exports = module.exports = function(zoomLevel, node, link) {
    if (zoomLevel < 12) {
      node.filter(function(d) {
          return d.object === "t_node";
        })
        .selectAll('rect')
        .attr('width', 10)
        .attr('x', -5)
        .attr('height', 2)
      link.filter(function(d) {
          return d.object === "transmission_line";
        })
        .style('stroke-width', 1)
    } else {
      node.filter(function(d) {
          return d.object === "t_node";
        })
        .selectAll('rect')
        .attr('width', 20)
        .attr('x', -10)
        .attr('height', 5);
      link.filter(function(d) {
        return d.object === "transmission_line";
        })
        .style('stroke-width', 2)
    }

    if (zoomLevel < 14) {
      node.filter(function(d) {
          return d.object === "centroid" || d.object === "t_node";
        })
        .style('display', 'inline')
        .style('opacity', .8);

      link.filter(function(d) {
        return d.linkType === "parentChild";
      })
        .style('display', 'inline')
        .style('opacity', .8)

      node.filter(function(d) {
          return d.object ==="node";
        })
        .style('display', 'inline');
    } else if (zoomLevel > 14) {
      link.filter(function(d) {
        return d.linkType === "parentChild";
      })
        .style('display', 'none');

      node.filter(function(d) {
          return d.object === "centroid" || d.object === "t_node";
        })
        .style('display', "none");

      node.filter(function(d) {
          return d.object ==="node";
        })
        .style('display', 'inline');
    } else {
      //13
      node.filter(function(d) {
          return d.object === "centroid" || d.object === "t_node";
        })
        .style('display', 'inline')
        .style('opacity', function(d) {
          if (d.name === "circuit1_centroid") {
            return 0;
          }
          return 0.8;
        });

      link.filter(function(d) {
        return d.linkType === "parentChild";
      })
        .style('opacity', function(d) {
          if (d.source.name === "circuit1_centroid" || d.target.name === "circuit1_centroid") {
            return 0;
          }
          return 0.8;
        });

      node.filter(function(d) {
          return d.object ==="node";
        })
        .style('display', 'inline');
    }
    //
    if (zoomLevel >= 15) {
      //TODO: ask roberts about that
      node.selectAll('.d_bus_title')
        .style("display", function() {
          // console.log(d3.select(this).text())
          return "inline";
        });
    } else {
      node.selectAll('.d_bus_title')
        .style("display", function() {
          // console.log(d3.select(this).text())
          return "none";
        });
    }
    //detail levle
    if (zoomLevel > 15) {
      //size of rect
      node.filter(function(d) {
          return d.object ==="node";
        })
        .selectAll('rect')
        .attr('width', function(d) {
          return 30;
        })
        .attr('x', function(d) {
          return -15;
        })
        .attr('height', function(d) {
          return 4;
        });
      //TODO: ask roberts about that
      node.selectAll('.elements')
        .style("display", function() {
          // console.log(d3.select(this).text())
          return "inline";
        });
    } else {
      node.filter(function(d) {
          return d.object ==="node";
        })
        .selectAll('rect')
        .attr('width', function(d) {
          return 10;
        })
        .attr('x', function(d) {
          return -5;
        })
        .attr('height', function(d) {
          return 2;
        });
      node.selectAll('.elements')
        .style("display", "none");
    }

    if (zoomLevel < 13) {
      node.filter(function(d) {
          return d.object === "centroid";
        })
        .style('display', 'none')
      link.filter(function(d) {
        return d.linkType === "parentChild";
      })
        .style('display', 'none')
    }

    // <= 13 transmission level
    if (zoomLevel < 1) {
      node.filter(function(d) {
        return d.object === "t_node";
      }).style('display', 'none');
    } else {
      node.filter(function(d) {
        return d.object === "t_node";
      }).style('display', 'inline');
    }
}