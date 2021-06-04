import React from 'react';
import {Container} from "react-bootstrap";
import Graph from "./Graph";

class Content extends React.Component {
  constructor(props){
    super(props);
  }

  render(){
    let content = (
        <Container fluid className="vh-100 bg-white">
          <Graph/>
        </Container>
    )

    return content;
  }
}

export default Content;