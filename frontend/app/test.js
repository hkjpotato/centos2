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




// Table data as a list of array.
var rows = [
  ['a1', 'b1', 'c1'],
  ['a2', 'b2', 'c2'],
  ['a3', 'b3', 'c3'],
];

var sorted = {
  name: 'name',
  order: 'desc'
}



var DashBoard = React.createClass({
  getInitialState: function() {
    return {
      sorted: {
        name: 'name',
        order: 'desc'
      }
    }
  },
  onClick: function(event) {
    console.log(event);
  },
  onMouseEnter: function(event) {
    console.log('enter', event.target);
    // this.refs[event.target.key].style.background = 'gray';
  },
  onMouseOut: function(event) {
    console.log('leave');
    // this.refs[event.target.key].style.background = 'white';
  },
  render: function() {
    var arr = ['name', 'age', 'id', 'ni', 'shi', 'shui', 'hehe', 'da', 'how', 'are', 'you'];
    var ths = arr.map(function(key) {
      return (
        <th key={key} onClick={this.onHeadClick}>
          {key}&nbsp;&nbsp;
          <i
            style={{
              opacity: (
                key === this.state.sorted.name ? 1 : 0.5
              )
            }}
            className={
            "fa fa-sort" + 
            (key === this.state.sorted.name ? 
              ("-" + this.state.sorted.order) : "")
          }>
          </i>
        </th>
      )
    }.bind(this));

    var rowData = new Array(100).fill(0);
    rowData.forEach(function(d, i) {
      rowData[i] = i + 1;
    });

    var rows = rowData.map(function(key) {
      return (
        <tr 
          key={key}
          ref={key + 'ref'}
          onClick={this.onClick} 
          onMouseEnter={this.onMouseEnter}
          onMouseOut={this.onMouseOut}
        >
          <td>{key}</td>
          <td>{key}</td>
          <td>{key}</td>
          <td>{key}</td>
          <td>{key}</td>
          <td>{key}</td>
          <td>{key}</td>
          <td>{key}</td>
          <td>{key}</td>
          <td>{key}</td>
          <td>{key}</td>
        </tr>
      )
    }.bind(this))

    return (
      <div>
        <div id='fake'>
          <table className='table table-bordered table-condensed table-striped table-hover'>
            <thead>
              <tr>
                {ths}
              </tr>
            </thead>
        </div>
        </table>
        <div id='real'>
        <table className='table table-bordered table-condensed table-striped table-hover' >
          <thead>
            <tr>
              {ths}
            </tr>
          </thead>
          <tbody>
            {rows}
          </tbody>
        </table>
        </div>
      </div>
    )
  }
})
//glue code with django template
window.MyApp = {
  init: function(data) {
    ReactDOM.render(
      <DashBoard style={{height: '100%'}}/>,
      document.getElementById('app')
    );
  }
}