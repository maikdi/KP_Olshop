<template>
  <div class="container-fluid">
    <Navbar></Navbar>
    <div class="row row-cols-4 row-cols-md-4 g-4">
      <div class="col" v-for="product in products" :key="product[0]">
        <div class="card" style="width: 18rem; margin-top:10px">
          <img :src="require('../assets/' + product[3])" class="card-img-top" />
          <div class="card-body">
            <p class="card-title"><b>{{ product[1] }}</b></p>
            <p class="card-text">
              Harga:
              {{
                new Intl.NumberFormat("in-IN", {
                  style: "currency",
                  currency: "IDR",
                }).format(product[2])
              }}
            </p>
            <a href="#" class="btn btn-primary">Details</a>
            <a href="#" class="btn btn-success">Add to cart</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
  data() {
    return {
      products: "",
    };
  },
  created() {
    fetch("http://localhost:5000/get_dashboard")
      .then((response) => {
        console.log(response);
        return response.json();
      })
      .then((data) => {
        this.products = data.data;
        console.log(data);
      });
  },
  methods: {},
};
</script>