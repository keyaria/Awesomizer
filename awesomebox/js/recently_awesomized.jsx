import React from 'react';
import PropTypes from 'prop-types';

class Recently_Awesomized extends React.Component {
  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {};
    this.state.books = [];

    this.handleClickMostAwesomized = this.handleClickMostAwesomized.bind(this);
  }

  componentDidMount() {
    // Call REST API to get number of likes
    fetch(this.props.url, { credentials: 'same-origin' })
    .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
    })
    .then((data) => {
        this.setState({
            books: data,
        });
    })
    .catch(error => console.log(error)); // eslint-disable-line no-console
  }

  handleClickMostAwesomized() {
    // Call REST API to get number of likes
    let url = this.props.url + "?sorted=True"
    fetch(url, { credentials: 'same-origin' })
    .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
    })
    .then((data) => {
        this.setState({
            books: data,
        });
    })
    .catch(error => console.log(error)); // eslint-disable-line no-console

    window.location.hash = "most-awesome";
  }

  render() {
    let outerDivStyle = {
      display:'inline-flex', 
      height:'200px', 
      width: '48%', 
      margin: '1% 1% 1% 1%', 
      border: '1px solid #aabbcc'
    };

    let imgStyle = {
      marginRight: '2%'
    };

    let innerDiv = {
      display: 'inline-block'
    };

    const booksRendered = this.state.books.map(book => (
      <div style={outerDivStyle} key={`${book.ISBN}`}>
        <img style={imgStyle} src={book.thumbnail}/>
        <div style={innerDiv}>
          <i>{book.title}</i><br/>
          by: {book.author_name} <br/>
          Times Scanned: {book.times_scanned}
        </div>
      </div>
    ));
    let index_className = "nav-item nav-link active";
    let most_awesome_className = "nav-item nav-link";
    let title = "RECENTLY AWESOMIZED";

    if (window.location.hash === "#most-awesome") {
      index_className = "nav-item nav-link";
      most_awesome_className = "nav-item nav-link active";
      title = "MOST AWESOMIZED";
    }
    return (
      <div>
      <h1 style={{textAlign: 'center'}}>{title}</h1>
      <nav className="navbar navbar-expand-lg navbar-light bg-light" style={{backgroundColor: '#60748F'}}>
        <a className="navbar-brand" href="/">The Awesomizer | Shapiro Design Lab</a>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav">
            <a className={index_className} href="/">Recently Awesomized</a>
            <a className={most_awesome_className} href="#most-awesome" onClick={this.handleClickMostAwesomized}>Most Awesomized</a>
            <a className="nav-item nav-link" href="/about">About</a>
          </div>
        </div>
      </nav>

      <br/>
      <div className="container-fluid">
        <h3> Recently Awesomized </h3>
      </div>
      <br/>
      {booksRendered}
      </div>
    );
  }
}

Recently_Awesomized.propTypes = {
  url: PropTypes.string.isRequired,
};

export default Recently_Awesomized;
