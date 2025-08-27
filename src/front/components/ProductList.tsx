'use client'; // Esta diretiva marca o componente como Client Component

import { useEffect, useState } from 'react';

// Defina uma interface para o tipo de dado do produto
interface Product {
  id: number;
  name: string;
  price: string;
}

export default function ProductList() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchProducts() {
      try {
        const apiUrl = process.env.NEXT_PUBLIC_API_URL;
        const response = await fetch(`${apiUrl}/catalog/products/`, {
          Authorization: Bearer 
        });

        if (!response.ok) {
          throw new Error('Falha ao buscar produtos');
        }

        const data: Product[] = await response.json();
        setProducts(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Um erro ocorreu');
      } finally {
        setLoading(false);
      }
    }

    fetchProducts();
  }, []); // O array vazio [] faz com que isso rode apenas uma vez

  if (loading) return <p>Carregando produtos...</p>;
  if (error) return <p>Erro: {error}</p>;

  return (
    <div>
      <h1>Lista de Produtos</h1>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.name} - R$ {product.price}
          </li>
        ))}
      </ul>
    </div>
  );
}