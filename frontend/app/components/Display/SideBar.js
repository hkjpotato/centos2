var React = require('react');
var Filter = require('./Filter');
var Preloader = require('./Preloader');
var ColorSelect = require('./ColorSelect');

var SideBar = React.createClass({
    getInitialState: function() {
        return {
            t_color: 'black',
            d_color: 'black'
        }
    },
    componentDidMount: function() {

    },
    render: function() {
        if (!this.props.data) {
            return <Preloader />
        } else {
            return (
                <div className="" style={{height: "100%"}}>
                    <div className="" style={{outline: "1px solid red", width: "100%"}}>
                        <h4>Vis Explorator</h4>
                    </div>
                    <div className="" style={{outline: "1px solid green", width: "100%"}}>
                        <Filter onFilterChange={this.props.onFilterChange} currFilter={this.props.filter} />
                    </div>
                    <div className="" style={{outline: "1px solid red", width: "100%"}}>
                        <ColorSelect 
                            tColor={this.props.tColor} 
                            dColor={this.props.dColor} 
                            onMapStyleChange={this.props.onMapStyleChange} 
                            onTColorChange={this.props.onTColorChange} 
                            onDColorChange={this.props.onDColorChange}/>
                    </div>
                    <div className="">
                        <button type="button" className="btn btn-block btn-danger" onClick={this.props.runAnalysis}>{this.props.status}</button>
                    </div>
                </div>
            )
        }
    }
});

module.exports = SideBar;
