import React from 'react';
import {Navbar, Nav, NavDropdown, Form, FormControl, Button, Container, InputGroup} from "react-bootstrap";

class Navigation extends React.Component {
  constructor(props){
    super(props);
  }

  render(){
    let navbar =(
        <Navbar bg="dark" variant="dark">
            <Container fluid className="d-flex h-100">
                <Nav>
                    <Navbar.Brand href="#home">LinkMaps</Navbar.Brand>
                    <Nav.Link href="#home">Wikipedia</Nav.Link>
                </Nav>

                <Nav className="justify-content-end">
                  <InputGroup>
                    <FormControl
                      placeholder="Title"
                      aria-label="Title"
                      aria-describedby="basic-addon2"
                    />
                    <InputGroup.Append>
                      <Button variant="outline-secondary">Explore</Button>
                    </InputGroup.Append>
                  </InputGroup>
                </Nav>
            </Container>
          </Navbar>
            )
    return navbar;
  }
}

export default Navigation;