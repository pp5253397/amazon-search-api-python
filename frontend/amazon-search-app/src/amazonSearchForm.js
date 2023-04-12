import { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import axios from 'axios';
import './searchform.css';

function AmazonSearchForm() {
  const [keyword, setKeyword] = useState('');
  const [products, setProducts] = useState([]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await axios.get(`http://127.0.0.1:5000/amazon_search?keyword=${keyword}`);
    setProducts(response.data);
  };

  return (
    <div className="SearchForm">
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="keyword">
          <Form.Label>Keyword</Form.Label>
          <Form.Control type="text" value={keyword} onChange={(event) => setKeyword(event.target.value)} />
        </Form.Group>
        <Button variant="primary" type="submit">
          Search
        </Button>
      </Form>
      <div className="products">
        {products.map((product) => (
          <div key={product.url} className="product">
            <h2>{product.title}</h2>
            <p>{product.price}</p>
            <p>{product.rating}</p>
            <a href={`https://www.amazon.in${product.url}`} target="_blank" rel="noreferrer">View on Amazon</a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AmazonSearchForm;
