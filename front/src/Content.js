import React from 'react';
import {Container} from "react-bootstrap";

class Content extends React.Component {
  constructor(props){
    super(props);
  }

  render(){
    let content = (
        <Container fluid className="h-100 bg-info">
          "asdasdasdasd"
        </Container>
    )

    return content;
  }
}

export default Content;