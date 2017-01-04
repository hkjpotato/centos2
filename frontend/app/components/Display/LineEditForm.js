var React = require('react');
var Configuration = require('./LineConfig/Configuration');

var LineEditForm = React.createClass({
    getInitialState: function() {
        var initialInfo = Object.assign({}, this.props.selectedInfo);
        // return {
        //     selectedInfo: initialInfo
        // }
        //use it as the state of this UI
        return initialInfo
    },
    componentDidUpdate: function() {
        var updateInfo = Object.assign({}, this.props.selectedInfo);
        this.setState({
            selectedInfo: updateInfo
        });
    },
    componentDidMount: function() {

    },
    onChange: function(e) {
        this.setState({
          [e.target.name] : e.target.value 
        });
    },
    saveData: function(e) {
      //   console.log('submit!', e);
      //   e.preventDefault();

      //   Object.keys(this.refs).forEach(function(key) {
      //       // formData[key] = this.refs.key.value;
      //       console.log(key);
      //       formData[key] = this.refs[key].value ? this.refs[key].value : null;

      //   }.bind(this));
      //   console.log('what is the form data', formData);
      //   var _self = this;

      // var type = 'd_' + (formData.object == 'node' ? 'buses': formData.object + 's');

      // //make ajax here using the id
      // var api = '/feeder/api/' + type + '/' + formData.id + '/';
      // $.ajax({
      //     type: "PUT",
      //     url: api,
      //     contentType: "application/json",
      //     data: JSON.stringify(formData),
      //     dataType: 'json',
      //     success: function(result) {
      //         console.log("success?", result);
      //       // _self.props.updateElement(Object.assign({}, _self.state.selectedInfo, result));
      //     }.bind(this)
      // });
    },
    render: function() {
        var inlineStyle = {
            position: 'absolute',
            top: 5,
            right: 5,
            width: 300,
            maxHeight: 500,
            border: '1px solid #009688',
            overflow: 'auto',
            background: 'white'
        }

        var lineInfo = this.state;
        var basicKeys = Object.keys(lineInfo).filter(function(key) {
            return key !== 'configuration';
            // return true;
        });
        var basicformGroupRows = basicKeys.map(function(key) {
            return (
              <div key={key} className="form-group form-group-sm row">
                <label className="col-xs-4 col-form-label" htmlFor={key}>{key}</label>
                <div className="col-xs-8">
                  <input 
                    id={key} 
                    className="form-control" 
                    value={lineInfo[key] ? lineInfo[key] : ''}
                    type="text" 
                    onChange={this.onChange} />
                </div>
              </div>
            )
        }.bind(this))
        return (
        <div className="row" style={inlineStyle}>
            <h4>Line Info</h4>
            <form onSubmit={this.saveData}>
                {basicformGroupRows}
                <Configuration
                    lineObject={lineInfo['object']}
                    keyName='configuration' 
                    value={lineInfo['configuration'] ? lineInfo['configuration']: ''}
                    onChange={this.onChange} />
                <div className="row">
                    <div className="col-xs-6">
                      <button className="btn" onClick={this.props.editStateChange}>Back</button>
                    </div>
                    <div className="col-xs-6">
                      <input className="waves-effect waves-light btn" type="submit" onChange={this.onChange} value="Confirm"/>
                    </div>
                </div>
            </form>
        </div>
        )
    }
});


module.exports = LineEditForm;
