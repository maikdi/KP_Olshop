<template>
  <div class="container-fluid">
    <Navbar class="row"></Navbar>
    <div id="cart-wrapper" class="row">
      <div id="parent-left" class="col-9 gx-3 gy-3">
        <div class="overflow-hidden p-4 border bg-light">
          <h5>Keranjang</h5>
          <ul class="list-group list-group-flush">
            <li
              class="list-group-item"
              v-for="product in products"
              :key="product[0]"
            >
              <div class="container">
                <div class="row row-cols-3">
                  <div class="col-1">
                    <img
                      :src="require('../assets/' + product[5])"
                      alt=""
                      style="width: 48px"
                      class="rounded"
                    />
                  </div>

                  <div class="col-10">
                    <em>{{ product[1] }}</em>
                    <div class="col">
                      <b>
                        {{
                          new Intl.NumberFormat("in-IN", {
                            style: "currency",
                            currency: "IDR",
                          }).format(product[2])
                        }}
                      </b>
                    </div>
                  </div>
                  <div class="col-1">
                    <button
                      type="button"
                      class="btn btn-sm btn-danger float-end"
                      @click="cancelItem(product)"
                    >
                      <b>X</b>
                    </button>
                  </div>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
      <div id="parent-right" class="col-3 gx-3 gy-3">
        <div class="overflow-hidden p-4 border bg-light">
          <h5>Total Pembelian</h5>
          <div class="d-flex w-100 justify-content-between">
            <p class="mb-1">Total Harga</p>
            <small>Rp. 131.000</small>
          </div>
          <div class="row centered">
            <button type="button" class="btn btn-success">Checkout</button>
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
      details: "",
      showModal: false,
    };
  },
  /* 
 REMEMBER TO CHANGE FETCH TO GET CART ITEMS 
  */
  created() {
    fetch("http://localhost:5000/get_dashboard")
      .then((response) => {
        // console.log(response);
        return response.json();
      })
      .then((data) => {
        this.products = data.data;
        this.$store.commit("setProducts", data.data);
        // console.log(data);
        this.toggleModal(0);
      });
  },
  methods: {
    toggleModal(index) {
      this.details = this.$store.getters.productDetails(index);
      this.showModal = true;
      document.getElementById("description").innerHTML = this.details[4];
      console.log(this.details);
    },
    addToCart(product) {
      console.log(product);
      this.$store.commit("addProductToCart", product);
    },
  },
};
</script>