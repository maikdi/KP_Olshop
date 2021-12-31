<template>
  <div class="container-fluid">
    <!-- Start Details Modal -->
    <div
      class="modal fade"
      id="exampleModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
      v-if="showModal"
      @close="showModal = false"
    >
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Detail Product</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div class="row">
              <div class="col">
                <img
                  :src="require('../assets/' + details[5])"
                  alt=""
                  style="width: 240px"
                />
              </div>
              <div class="col">
                <b>{{ details[1] }}</b>
                <p>
                  Harga:
                  {{
                    new Intl.NumberFormat("in-IN", {
                      style: "currency",
                      currency: "IDR",
                    }).format(details[2])
                  }}
                </p>
                <br />
                <p>Kategori: {{ details[3] }}</p>
                <p>Deskripsi:</p>
                <br />
                <p id="description"></p>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- End Details MODAL -->
    <!-- Start Cart Modal -->
    <div
      class="modal fade"
      id="cartModal"
      tabindex="-1"
      aria-labelledby="cartSuccess"
      aria-hidden="true"
      v-if="showModal"
      @close="showModal = false"
    >
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="cartSuccess">
              Produk berhasil masuk keranjang!
            </h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">Produk berhasil masuk keranjang! :D</div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary me-2 col-auto"
              data-bs-dismiss="modal"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- End Cart Modal -->
    <Navbar class="row" v-on:search="search"></Navbar>
    <div class="row row-cols-4 row-cols-md-4 g-4">
      <div class="col" v-for="product in products" :key="product[0]">
        <div class="card border-dark mb-3 h-80">
          <img
            :src="require('../assets/' + product[5])"
            class="card-img-top"
            style="height: 300px"
          />
          <div class="card-body">
            <p
              class="card-title"
              style="
                overflow: hidden;
                text-overflow: ellipsis;
                display: -webkit-box;
                -webkit-line-clamp: 2;
                line-clamp: 2;
                -webkit-box-orient: vertical;
              "
            >
              <b>{{ product[1] }}</b>
            </p>
            <p class="card-text">
              Harga:
              {{
                new Intl.NumberFormat("in-IN", {
                  style: "currency",
                  currency: "IDR",
                }).format(product[2])
              }}
            </p>
          </div>
          <div class="card-footer">
            <a
              href="#"
              class="btn btn-primary me-5"
              data-bs-toggle="modal"
              data-bs-target="#exampleModal"
              v-on:click="[toggleModal(product[0] - 1), showDetails=true]"
              >Details</a
            >
            <a
              href="#/cart"
              class="btn btn-success col-auto"
              data-bs-toggle="modal"
              data-bs-target="#cartModal"
              @click="addToCart(product)"
              ><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cart4" viewBox="0 0 16 16">
  <path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l.5 2H5V5H3.14zM6 5v2h2V5H6zm3 0v2h2V5H9zm3 0v2h1.36l.5-2H12zm1.11 3H12v2h.61l.5-2zM11 8H9v2h2V8zM8 8H6v2h2V8zM5 8H3.89l.5 2H5V8zm0 5a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"/>
</svg> Add to cart</a
            >
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
      showDetails: false,
    };
  },
  created() {
    if (this.$session.has('admin')){
      this.$router.push({
        path : "/admin"
      })
    } 
    fetch("http://localhost:5000/get_dashboard")
      .then((response) => {
        // console.log(response);
        return response.json();
      })
      .then((data) => {
        this.products = data.data;
        this.$store.commit("setProducts", data.data);
        if (this.$session.has("user")){
          this.username = this.$session.get("user")
        }
        // console.log(data);
        this.toggleModal(0);
      });
  },
  methods: {
    toggleModal(index) {
      this.details = this.$store.getters.productDetails(index);
      this.showModal = true;
      document.getElementById("description").innerHTML = this.details[4];
    },
    addToCart(product) {
      this.$store.commit("addCart", product);
      console.log(this.$store.getters.getCart);
    },
    goToCart() {
      this.$router.push({
        path: "/cart",
      });
    },
    search(keyword) {
      let options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(keyword),
      };
      fetch("http://localhost:5000/search-product", options)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.products = data.data;
        });
    },
  },
};
</script>

<style scoped>
.card {
  width: 18rem;
  margin-top: 10px;
  border-radius: 10px;
  box-shadow: 0 3px 6px 0 var(--N700, rgba(49, 53, 59, 0.12));
}
</style>