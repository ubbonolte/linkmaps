import React from 'react'
import {Helmet} from 'react-helmet'

import './App.css';

import Navigation from './Navbar'
import Content from './Content'
import {Container, Row, Col} from "react-bootstrap";


class App extends React.Component {
  render () {
    return (
        <div className="application">
            <Helmet>
                <meta charSet="utf-8" />
                <title>Explore LinkMaps</title>
            </Helmet>
            <Container fluid className="h-100 w-100">
                <Navigation />
                <Content />
            </Container>
        </div>
    );
  }
};

export default App;
