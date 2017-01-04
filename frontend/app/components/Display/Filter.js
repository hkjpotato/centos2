var React = require('react');
var eleColorMap = require('./Helpers/ElementHelper').eleColorMap;
var iconClassName = require('./Helpers/ElementHelper').iconClassName;

var Filter = React.createClass({
  filterClick: function(event) {
      var filter = event.target.value.toLowerCase();
      this.props.onFilterChange(this.props.currFilter == filter ? null : filter);
  },
  render: function() {
    var currFilter = this.props.currFilter
    //arrange them in order of load/generator/storage/solar/capacitor
    var items = ['load', 'generator', 'storage', 'solar', 'capacitor'];

    var filters = items.map(function(object, i) {
      return (
        <div className="checkbox" key={i}>
          <label>
            <input 
              type="checkbox" 
              checked={object==currFilter}
              value={object}
              onChange={this.filterClick} />
          <i 
            style={{color: eleColorMap[object]}} 
            className={iconClassName[object]} 
            aria-hidden="true">
          </i>
          {object}
          </label>
        </div>
      )
    }.bind(this));
    return (
      <div 
        className="kj_panel"
        ref="mountPoint" >
        <div 
          className="kj_title">
            filter
        </div>
        <div className="kj_content">
          {filters}
        </div>
      </div>
    );
  }
});

module.exports = Filter;