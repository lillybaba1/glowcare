import os
import requests
import streamlit as st

API_URL = os.getenv('API_URL', 'http://localhost:8000')

st.title('Product Manager')

# List products
st.header('Products')
try:
    resp = requests.get(f"{API_URL}/products")
    resp.raise_for_status()
    products = resp.json()
except Exception as e:
    st.error(f"Error fetching products: {e}")
    products = []

if products:
    for product in products:
        st.write(f"{product}")
else:
    st.write("No products found.")

st.header('Add Product')
with st.form('add_product'):
    name = st.text_input('Name')
    description = st.text_area('Description')
    submitted = st.form_submit_button('Add')
    if submitted:
        try:
            resp = requests.post(f"{API_URL}/products", json={"name": name, "description": description})
            resp.raise_for_status()
            st.success('Product added')
        except Exception as e:
            st.error(f"Error adding product: {e}")

st.header('Delete Product')
with st.form('delete_product'):
    product_id = st.text_input('Product ID')
    delete_submitted = st.form_submit_button('Delete')
    if delete_submitted:
        try:
            resp = requests.delete(f"{API_URL}/products/{product_id}")
            if resp.status_code == 200:
                st.success('Product deleted')
            else:
                st.error(f"Delete failed: {resp.text}")
        except Exception as e:
            st.error(f"Error deleting product: {e}")
