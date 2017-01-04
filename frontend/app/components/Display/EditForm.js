var React = require('react');
var EditForm = React.createClass({
    getInitialState: function() {
        var initialInfo = Object.assign({}, this.props.selectedInfo);
        return {
            selectedInfo: initialInfo
        }
    },
    componentDidUpdate: function() {
        var updateInfo = Object.assign({}, this.props.selectedInfo);
        this.setState({
            selectedInfo: updateInfo
        });
    },
    componentDidMount: function() {
    },
    handleChange: function(event) {
        console.log('calling the edit form select', event.target.id);
        return;
        var currInfo = this.state.selectedInfo;
        currInfo[event.target.id] = event.target.value;
        this.setState({
            selectedInfo: currInfo
        });
    },
    saveData: function(e) {
        console.log('submit!', e);
        e.preventDefault();
        console.log(this.refs);
        var formData = {};
        Object.keys(this.refs).forEach(function(key) {
            // formData[key] = this.refs.key.value;
            console.log(key);
            formData[key] = this.refs[key].value ? this.refs[key].value : null;

        }.bind(this));
        console.log('what is the form data', formData);
        var _self = this;

      var type = 'd_' + (formData.object == 'node' ? 'buses': formData.object + 's');

      //make ajax here using the id
      var api = '/feeder/api/' + type + '/' + formData.id + '/';
      $.ajax({
          type: "PUT",
          url: api,
          contentType: "application/json",
          data: JSON.stringify(formData),
          dataType: 'json',
          success: function(result) {
              console.log("success?", result);
            // _self.props.updateElement(Object.assign({}, _self.state.selectedInfo, result));
          }.bind(this)
      });
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
        var selectedInfo = this.state.selectedInfo;
        var keys = Object.keys(selectedInfo);

        var formGroupRows = keys.map(function(key) {
            return (
              <div key={key} className="form-group form-group-sm row">
                <label className="col-xs-4 col-form-label" htmlFor={key}>{key}</label>
                <div className="col-xs-8">
                  <input className="form-control" ref={key} defaultValue={selectedInfo[key]} id={key} type="text" onChange={this.handleChange} />
                </div>
              </div>
            )
        }.bind(this))
        return (
        <div className="row" style={inlineStyle}>
            <form onSubmit={this.saveData}>
                {formGroupRows}
                <div className="row">
                    <div className="col-xs-6">
                      <button className="btn" onClick={this.props.editStateChange}>Back</button>
                    </div>
                    <div className="col-xs-6">
                      <input className="waves-effect waves-light btn" type="submit" onChange={this.handleChange} value="Confirm"/>
                    </div>
                </div>
            </form>
        </div>
        )
    }
});




module.exports = EditForm;
