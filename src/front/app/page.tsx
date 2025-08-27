'use client'

import Header from "@/components/Header";
import ProductList from "@/components/ProductList";

export default function Home() {
  return (
    <>
      <Header />
      <main>
        <h1>Welcome to the Home Page</h1>
        <p>This is the main content area.</p>
        <ProductList />
      </main>
    </>
  );
}
