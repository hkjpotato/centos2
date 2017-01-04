//App.js
//our app js now become a glue code for django
var React = require('react');
var ReactDOM = require('react-dom');
var VisContainer = require('./components/Display/VisContainer');
var Filter = require('./components/Display/Filter');
var Preloader = require('./components/Display/Preloader');
var FilterableElementTable = require('./components/Display/FilterableElementTable');
var PopTable = require('./components/Display/PopTable');

var RunningLoader = require('./components/Display/RunningLoader');
var SideBar = require('./components/Display/SideBar');
var SearchBar = require('./components/Display/SearchBar');

var transmissionData = null;
var playInterval = null;
var currentFeeder = "null";
var currViewLevel = 'transmission';

var DashBoard = React.createClass({
  onViewChange: function(updateMapProps) {
    var updateZoomLevel = updateMapProps.zoomLevel;
    var updateMapCenter = updateMapProps.mapCenter;
    // This is for demo purpose, in the real app, should make the query based on  zoomLevel
    var apiAddress = "";
    var shouldUpdateData = false;
    var updateViewLevel = (updateZoomLevel < 14 ) ? 'transmission' : 'distribution';
    if (updateViewLevel !== currViewLevel) {
        console.log('!!!!!!!--------VIEW LEVEL CHANGE--------!!!!!!!');
        currViewLevel = updateViewLevel;
        shouldUpdateData = true;
    }
    if (shouldUpdateData) {
        var apiAddress = "/feeder/feederData/?zoomLevel=" + updateZoomLevel;
        d3.json(apiAddress, function (json) {
          this.setState({
            data: json,
            dataChange: true,
          });
        }.bind(this));
    }
  },
  getInitialState: function() {
    return {
      editing: false,
      data: null,
      selected: null,
      filter: null,
      viewMode: 'vis',
      process: 'ready',
      playing: false,
      timeVal: 1,
      tColor: 'aqua',
      dColor: 'white',
      mapStyle: 'satellite',
      mapProps: {
        zoomLevel: 11,
        mapCenter: new google.maps.LatLng(41.0699044, -71.909294)
      },
      dataChange: false,
      multiSelectMap: null,
      hovering: null,
      popUp: false
    }
  },
  onMapStyleChange: function(mapStyle) {
    this.setState({
      mapStyle: mapStyle
    });
  },
  onTColorChange: function(tColor) {
    this.setState({
      tColor: tColor
    });
  },
  onDColorChange: function(dColor) {
    this.setState({
      dColor: dColor
    });
  },
  hoverCb: function(d) {
    this.setState({
      hovering: d
    })
  },
  onSelectChange: function(d) {
    if (!d) {
      this.setState({
        selected: null,
        dataChange: false,
        editing: false
      });
      return;
    }
    if (d && d.object === "centroid") {
      console.log('NO WAY!')
    } else {
      console.log('DashBoard onSelectChange, id: ', d.id);
      var type = 'd_' + (d.object == 'node' ? 'buses': d.object + 's');
      //make ajax here using the id
      var api = '/feeder/api/' + type + '/' + d.id;
      $.ajax({
          type: "GET",
          url: api,
          contentType: "application/json",
          success: function(result) {
              this.setState({
                selected: result,
                dataChange: false,
                editing: false
              });
          }.bind(this)
      });
    }
  },
  onTimeChange: function(timeVal) {
    this.setState({
      timeVal: timeVal
    });
  },
  updateElement: function(data) {
    //ajax
    //update state
    var currpgObj = this.state.data;
    
    currpgObj[data.gldIndex] = data;
    this.setState({
      data: currpgObj,
      dataChange: true,
      // selected: null
    });
  },
  removeElement: function(data) {
    //ajax
    //update state
    var newIndex = 2000;
    var newEle = {
      gldIndex: 2000,
      object: data.eleObj,
      name: "hkjpotato",
      parent: data.parent,
    };
    var currpgObj = this.state.data;
    currpgObj[newIndex] = newEle;
    this.setState({
      data: currpgObj,
      dataChange: true
    });
  },
  editStateChange: function(data) {
    console.log('edit state change')
    this.setState({
      editing: !this.state.editing
    });
  },
  onPlayClick: function() {
    if (!this.state.playing) {
        clearInterval(playInterval);
        playInterval = setInterval(function() {
            var currValue = this.state.timeVal;
            this.setState({
                timeVal: (((currValue + 1) - 1) % 24 + 1)
            })
        }.bind(this), 2000);
    } else {
        clearInterval(playInterval);
    }
    this.setState({
        playing: !this.state.playing
    });
  },
  onFilterChange: function(d) {
    console.log('DashBoard onFilterChange: ', d)
    this.setState({
      filter: d,
      dataChange: false
    });
  },
  componentDidMount: function() {
    self = this;
    // $('ul.tabs').tabs({
    //   onShow: function(event) {
    //     self.setState({
    //       viewMode: $(event).attr('id')
    //     });
    //   }
    // });
    //for demo purpose
    var apiAddress = "/feeder/feederData/?zoomLevel=" + this.state.mapProps.zoomLevel;
    d3.json(apiAddress, function (json) {
      var pgObject = json;
      console.log(pgObject)
      this.setState({
        data: json,
        dataChange: true
      });
    }.bind(this));
  },
  runAnalysis: function() {
    if (this.state.process == "finished") {
      this.setState({
        process: 'ready'
      })
    } else {
      this.setState({
        process: 'running'
      });
      setTimeout(function() {
        this.setState({
          process: 'finished'
        });
        }.bind(this), 3000);
      }
  },
  popUpChange: function() {
    this.setState({
      popUp: !this.state.popUp,
    })
  },
  render: function() {
    var status = this.state.process === "ready" ? "run" : this.state.process;
    return (
        <div className="container-fluid" style={{height: '100%'}}>
          <div className="row" style={{height: '100%'}}>
            <div className="col-sm-2" style={{height: '100%'}}>
              <SideBar 
                tColor={this.state.tColor} 
                dColor={this.state.dColor}
                mapStyle={this.state.mapStyle}
                onMapStyleChange={this.onMapStyleChange} 
                onTColorChange={this.onTColorChange} 
                onDColorChange={this.onDColorChange} 
                status={status} 
                runAnalysis={this.runAnalysis}data={this.state.data} 
                onFilterChange={this.onFilterChange} 
                filter={this.state.filter} />
            </div>
            <div className="col-sm-10" style={{height: '100%'}}>
              <div id="vis" style={{height: '100%'}}>
                <VisContainer 
                  height={this.state.popUp ? '60%' : '100%'} 
                  hovering={this.state.hovering}
                  multiSelectMap={this.state.multiSelectMap}
                  mapStyle={this.state.mapStyle} 
                  tColor={this.state.tColor} 
                  dColor={this.state.dColor} 
                  updateElement={this.updateElement}
                  editStateChange={this.editStateChange} 
                  onPlayClick={this.onPlayClick} 
                  onTimeChange={this.onTimeChange} 
                  timeVal={this.state.timeVal} 
                  playing={this.state.playing} 
                  process={this.state.process} 
                  dataChange={this.state.dataChange} 
                  mapProps={this.state.mapProps} 
                  data={this.state.data} 
                  onSelectChange={this.onSelectChange}  
                  onViewChange={this.onViewChange}  
                  onFilterChange={this.onFilterChange} 
                  selected={this.state.selected}
                  editing={this.state.editing} 
                  filter={this.state.filter} />

                <button style={{position: 'absolute', top: 100}} onClick={this.popUpChange}>pop</button>

                {this.state.popUp ? (
                  <PopTable 
                    hoverCb = {this.hoverCb}
                    hovering={this.state.hovering}
                    multiSelectMap={this.state.multiSelectMap}
                    data={this.state.data} 
                    height={'40%'} 
                    selected={this.state.selected} 
                    filter={this.state.filter} 
                    viewMode={this.state.viewMode} 
                    onSelectChange={this.onSelectChange} />
                  ) : null}

              </div>
            </div>
          </div>
        </div>
      )
  }
})

                  // <button style={{position: 'absolute', top: 100}} onClick={this.popUpChange}>pop</button>

                  // {this.state.popUp ? (
                  //   <PopTable 
                  //     hoverCb = {this.hoverCb}
                  //     hovering={this.state.hovering}
                  //     multiSelectMap={this.state.multiSelectMap}
                  //     data={this.state.data} 
                  //     height={'40%'} 
                  //     selected={this.state.selected} 
                  //     filter={this.state.filter} 
                  //     viewMode={this.state.viewMode} 
                  //     onSelectChange={this.onSelectChange} />
                  //   ) : null}
    
    //  <div className="row" style={{height: '100%'}}>
    //   <div className="col-sm-2" style={{height: "100%"}}>
    //     <SideBar 
    //       tColor={this.state.tColor} 
    //       dColor={this.state.dColor}
    //       mapStyle={this.state.mapStyle}
    //       onMapStyleChange={this.onMapStyleChange} 
    //       onTColorChange={this.onTColorChange} 
    //       onDColorChange={this.onDColorChange} 
    //       status={status} 
    //       runAnalysis={this.runAnalysis}data={this.state.data} 
    //       onFilterChange={this.onFilterChange} 
    //       filter={this.state.filter} />
    //   </div>
    //   <div className="col-sm-10" style={{height: '100%'}}> 
    //      <div className="row" style={{height: '100%', position: 'relative'}}>
    //         <div className="col-sm-4">
    //           <ul className="tabs">
    //             <li className="tab col-sm-2"><a href="#vis" className="active">Vis</a></li>
    //             <li className="tab col-sm-2"><a href="#table">Table</a></li>
    //           </ul>
    //         </div>
    //         <div className="col-sm-4 col-sm-offset-4">
    //           <SearchBar />
    //         </div>
    //         {this.state.process === "running" ?  
    //           <RunningLoader /> : null
    //         }
    //         <div id="vis" style={{height: '90%'}} className="col-sm-12">
    //           <VisContainer 
    //             height={this.state.popUp ? '60%' : '100%'} 
    //             hovering={this.state.hovering}
    //             multiSelectMap={this.state.multiSelectMap}
    //             mapStyle={this.state.mapStyle} 
    //             tColor={this.state.tColor} 
    //             dColor={this.state.dColor} 
    //             updateElement={this.updateElement}
    //             editStateChange={this.editStateChange} 
    //             onPlayClick={this.onPlayClick} 
    //             onTimeChange={this.onTimeChange} 
    //             timeVal={this.state.timeVal} 
    //             playing={this.state.playing} 
    //             process={this.state.process} 
    //             dataChange={this.state.dataChange} 
    //             mapProps={this.state.mapProps} 
    //             data={this.state.data} 
    //             onSelectChange={this.onSelectChange}  
    //             onViewChange={this.onViewChange}  
    //             onFilterChange={this.onFilterChange} 
    //             selected={this.state.selected}
    //             editing={this.state.editing} 
    //             filter={this.state.filter} />
                
    //             <button style={{position: 'absolute', top: 100}} onClick={this.popUpChange}>pop</button>

    //             {this.state.popUp ? (
    //               <PopTable 
    //                 hoverCb = {this.hoverCb}
    //                 hovering={this.state.hovering}
    //                 multiSelectMap={this.state.multiSelectMap}
    //                 data={this.state.data} 
    //                 height={'40%'} 
    //                 selected={this.state.selected} 
    //                 filter={this.state.filter} 
    //                 viewMode={this.state.viewMode} 
    //                 onSelectChange={this.onSelectChange} />
    //               ) : null}
    //         </div>

    //         <div id="table" style={{height: '90%'}} className="col-sm-12">
    //           {this.state.viewMode === 'table' ? (
    //             <FilterableElementTable 
    //               hoverCb = {this.hoverCb}
    //               multiSelectMap={this.state.multiSelectMap}
    //               data={this.state.data} 
    //               selected={this.state.selected} 
    //               filter={this.state.filter} 
    //               viewMode={this.state.viewMode} 
    //               onSelectChange={this.onSelectChange} />
    //           ) : null}
    //         </div>
    //       </div>
    //   </div>
    // </div>

//glue code with django template
window.MyApp = {
  init: function(data) {
    ReactDOM.render(
      <DashBoard style={{height: '100%'}}/>,
      document.getElementById('app')
    );
  }
}