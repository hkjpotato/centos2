var React = require('react');
var Chart = require('./KjChart');
var options = require('./Helpers/ChartOptions').options;


var TimeSlider = React.createClass({
  onChange: function(event) {
    this.props.onTimeChange(+event.target.value);
  },
  onPlayClick: function(event) {
    this.props.onPlayClick();

  },
  render: function() {
    var inlineStyle = {
        position: 'absolute',
        bottom: 5,
        left: 0,
        right: 0,
        marginLeft: 'auto',
        marginRight: 'auto',
        width: 580,
        height: 120,
        border: '1px solid #367ebd',
        borderRadius: '1%',
        overflow: 'auto',
        background: 'white',
        // paddingTop: 0,
        padding: '0 5px',

        zIndex: 3,
    };
    var playButtonStyle = {
        display: 'inline-block',
        margin: 5,
        marginTop: 50,
        cursor: "pointer",
        fontSize: '250%',
        float: 'left'
    }
    var sliderStyle = {
        display: 'inline-block',
        margin: 10,
        float: 'left',
        width: 500
    }

    var playing = this.props.playing;
    var timeVal = this.props.timeVal;
    return (
        <div style={inlineStyle} className="kj_panel">
            <a style ={playButtonStyle} onClick={this.onPlayClick} className="">
                <i className={"fa fa-" + (playing ? "pause" : "play") + "-circle-o"} aria-hidden="true"></i>
            </a>
            <div style ={sliderStyle}>
              <div id="kjchart" style={{marginBottom: '-75px', zIndex: -1, pointerEvents: 'none'}}>
                <Chart container="kjchart" options={options} />
              </div>
              <div id="timeControl" style={{zIndex: 10}}>
                <input type="range" id="test5" step="1" min="1" max="24" value={timeVal} onChange={this.onChange}/>
              </div>
            </div>
        </div>
    )
  }
});



module.exports = TimeSlider;