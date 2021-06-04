import React from 'react';
import CytoscapeComponent from 'react-cytoscapejs';


class Graph extends React.Component {
  constructor(props){
    super(props);
    this.state = {
        error: null,
        isLoaded: false,
        elements: {},
    }
  }

  componentDidMount() {
      this.get_graph()
      this.render()
  }

  get_graph(title){
      fetch("http://127.0.0.1:5000/wiki/en/Penis")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            elements: JSON.parse(result)
          });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }

  render(){
      const { error, isLoaded, items } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
    <CytoscapeComponent elements={this.state.elements.nodes.concat(this.state.elements.edges)} style={ { width: '100%', height: '100%' } } />
      );
    }
  }
}

export default Graph;