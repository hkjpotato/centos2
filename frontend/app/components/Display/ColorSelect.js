var React = require('react');
var colorOptions = require('./Helpers/CustomizeHelper').colorOptions;

var ColorSelect = React.createClass({
    onTColorChange: function(event) {
        event.preventDefault();
        this.props.onTColorChange(event.target.value);
    },
    onDColorChange: function(event) {
        event.preventDefault();
        this.props.onDColorChange(event.target.value);
    },
    onMapStyleChange: function(event) {
        event.preventDefault();
        this.props.onMapStyleChange(event.target.value);
    },
    render: function() {      
        var options = colorOptions.map(function(d) {
          return (<option key={d} value={d}>{d}</option>);
        })
        return (
            <div 
              className="kj_panel" id="selectCotainer">
              <div
                className="kj_title">
                customization
              </div>
              <div className="kj_content">
                <form className="form">
                  <div className="form-group">
                    <label className="lb-sm" htmlFor="map_style_select">{"Map Style"}</label>
                    <select 
                      className="form-control input-sm" 
                      id="map_style_select" 
                      value={this.props.mapStyleId}
                      onChange={this.onMapStyleChange}>
                      <option value="satellite">satellite</option>
                      <option value="roadmap">roadmap</option>
                      <option value="hybrid">hybrid</option>
                      <option value="terrain">terrain</option>
                      <option value="light">light</option>
                      <option value="plain">plain</option>
                      <option value="dark">dark</option>
                      <option value="night">night</option>
                    </select>
                  </div>

                  <div className="form-group">
                    <label className="lb-sm" htmlFor="t_color_select">Transmission Color</label>
                    <select 
                      className="form-control input-sm"
                      id="t_color_select" 
                      value={this.props.tColor}
                      onChange={this.onTColorChange}>
                      {options}
                    </select>
                  </div>

                  <div className="form-group">
                    <label className="lb-sm" htmlFor="d_color_select">Distribution Color</label>
                    <select
                      className="form-control input-sm"
                      id="d_color_select" 
                      value={this.props.dColor}
                      onChange={this.onDColorChange}>
                      {options}
                    </select>
                  </div>
                </form>
              </div>
            </div>
        )
    }
});

module.exports = ColorSelect;

