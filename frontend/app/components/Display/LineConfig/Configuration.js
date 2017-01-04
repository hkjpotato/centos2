var React = require('react');
var Configuration = React.createClass({
    getInitialState: function() {
        return {
            configList: [],
            expand: false
        }
    },
    componentDidMount: function() {
        var api = '/feeder/api/d_ohl_configurations/';
        $.getJSON(api, function(data) {
          this.setState({
            configList: data,
          });
        }.bind(this));
    },
    updateList: function(action) {
        var configApi = this.props.lineObject === 'overhead_line' ? 'd_ohl_configurations' : null
        var api = '/feeder/api/' + + '/';
        $.getJSON(api, function(data) {
            console.log('ready to update the list', data, this.props);
            this.setState({
                configList: data
            });
            switch (action.type) {
                case "create":
                    this.props.onChange({
                        target: {
                            name: 'configuration',
                            value: action.id
                        }
                    })
                    break;
                case "update":
                    this.props.onChange({
                        target: {
                            name: 'configuration',
                            value: action.id
                        }
                    })
                    break;
                case "delete":
                    var lastId = this.state.configList[this.state.configList.length - 1].id;
                    console.log('delete so set last id: ', lastId)
                    this.props.onChange({
                        target: {
                            name: 'configuration',
                            value: ''
                        }
                    })
                    break;
                default:
                    console.log('default action, updateList');
            }
        }.bind(this));
    },
    toggleExpand: function() {
        this.setState({
          expand: !this.state.expand
        });
    },
    render: function() {
        var options = this.state.configList.map(function(config) {
            return (
                <option key={config.id} value={config.id}>
                  {config.name}
                </option>
            );
        });

        options.push(
            <option key={'no-value'} value={''}>
              {'None'}
            </option>
        );

        var search = this.state.configList.filter(function(config) {
            return config.id == this.props.value
        }.bind(this));

        var configInfo = search.length > 0 ? search[0] : null;

        return (
            <div className="form-group form-group-sm row">
                <label className="col-xs-4 col-form-label" htmlFor={this.props.keyName}>{this.props.keyName.replace(/_/g, ' ')}</label>
                <div className="col-xs-8">
                    <select
                        id={this.props.keyName} 
                        className="form-control" 
                        value={this.props.value} 
                        onChange={this.props.onChange}>
                      {options}
                    </select>
                </div>


            </div>
        );
    }
});
module.exports = Configuration;