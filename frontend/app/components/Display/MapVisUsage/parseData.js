
exports = module.exports = function(data, nodes, links) {
    //the passed in data is props, should not use them directly to make the link
    //have to create new nodes and links and elements from the props
    var pgObject = data;
    var name2eleMap = {};
    console.log("^^^CRAZY PARSE DATA DUE TO DATA CHANGE^^^");
    //at this moment, we always clear the data
    // nodes = [];
    // links = [];
    nodes.length = 0;
    links.length = 0;
    // console.log('parseData', pgObject);
    //parse data into the nodes and links

    for (var x in pgObject) {
        // break;
        //in a tree, if an element has either name or module but from is undefined, it must be a node
        if ((pgObject[x].name != undefined || pgObject[x].module != undefined) && pgObject[x].from == undefined) {
            var nodeName = pgObject[x].name;
            var nodeObject = pgObject[x].object;
            //only regard d_bus as a node
            if (nodeObject === "node" || nodeObject === "t_node") {
              var newNode = {
                  gldIndex: parseInt(x),
                  name: nodeName,
                  object: nodeObject,
                  lat: pgObject[x].lat,
                  lng: pgObject[x].lng,
                  elements: {}
              };
              Object.assign(newNode, pgObject[x]);
              //ATTENTION: this is anti-pattern, should not modify the props by children
              nodes.push(newNode)
              name2eleMap[nodeName] = newNode;
            }
            if (nodeObject === "centroid") {
              var newNode = {
                  gldIndex: parseInt(x),
                  name: nodeName,
                  object: nodeObject,
                  lat: pgObject[x].lat,
                  lng: pgObject[x].lng,
                  elements: {}
              };
              nodes.push(newNode);
              name2eleMap[nodeName] = newNode;
            }
        }
    }
    // Go through a second time and set up the links:
    for (var x in pgObject) {
        // break;
        // in a pgObject, if an element has name
        if (pgObject[x].name != undefined) {
            //then if it has from to, it is a fromto link
            if (pgObject[x].from != undefined && pgObject[x].to != undefined) {
                links.push({
                    source: name2eleMap[pgObject[x].from],
                    target: name2eleMap[pgObject[x].to],
                    object: pgObject[x].object,
                    linkType: 'fromTo',
                    id: pgObject[x].id
                })
            } 
            else if (pgObject[x].parent != undefined) {
                if (pgObject[x].object == "centroid") {
                  //else if it has parent, it is a parentChild link
                  links.push({
                      source: name2eleMap[pgObject[x].parent],
                      target: name2eleMap[pgObject[x].name],
                      linkType: 'parentChild'
                  });
                } else {
                  //it is an element, attach the data to the right element
                  var parentNode = name2eleMap[pgObject[x].parent];
                  // var nodeName = pgObject[x].name;
                  var eleObject = pgObject[x].object;
                  //directly using the json data from server
                  var newEle = {};
                  Object.assign(newEle, pgObject[x]);
                  parentNode.elements[eleObject]
                    = newEle;
                }
            }
        }
    }
}