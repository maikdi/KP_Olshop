<template>
  <div class="justify-content-center">
    <!-- Start Login Modal -->
    <div
      class="modal fade"
      id="loginModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
      v-if="showModal"
      @close="showModal = false"
    >
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Login</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <Login v-on:valid="createInvoice"></Login>
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
    <!-- End Login MODAL -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <!-- DIV FOR LOGO AND TABS -->
      <div class="container-fluid">
        <a class="navbar-brand">Navbar</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNavDropdown"
          aria-controls="navbarNavDropdown"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a
              class="nav-link active"
              aria-current="page"
              href="#/admin"
              v-if="isAdmin"
              >Products</a
            >
            <a
              class="nav-link active"
              aria-current="page"
              href="#/"
              @click="goHome"
              v-else
              >Home</a
            >
          </li>
          <li class="nav-item">
            <a
              class="nav-link active"
              aria-current="page"
              href="#/sale-report"
              v-if="isAdmin"
              >Sales Report</a
            >
            <a
              class="nav-link active"
              aria-current="page"
              href="#/cart"
              @click="createInvoice"
              v-if="this.$session.has('user') "
              >Keranjang</a
            >
            <a
              class="btn btn-link nav-link active"
              aria-current="page"
               @click="toLogin" data-bs-toggle="modal" data-bs-target="#loginModal"
              v-if="!this.$session.has('user') && !this.$session.has('admin')"
              >Keranjang</a
            >
          </li>
        </ul>
      </div>
      <!-- DIV FOR SEARCH BAR ONLY -->
      <div class="container-fluid" v-if="!isAdmin">
          <input
            class="form-control me-2 col-auto"
            type="search"
            placeholder="Search"
            aria-label="Search"
            v-model="keyword"
          />
          <button class="btn btn-outline-light" type="submit" @click="$emit('search', keyword)">Search</button>
      </div>
      <!-- DIV FOR USER SECTION -->
      <div class="container-fluid"></div>
      <div class="d-flex" v-if="loginStatus">
        <a class="btn btn-outline-light me-2 col-auto" aria-current="page">
          {{ this.username }}
        </a>
        <a class="btn btn-outline-light" aria-current="page" @click="logout">
          Logout
        </a>
      </div>
      <div v-else>
        <a class="btn btn-outline-light" aria-current="page" @click="toLogin" data-bs-toggle="modal" data-bs-target="#loginModal">
          Login
        </a>
      </div>
    </nav>
  </div>
</template>

<script>
import Login from './views/Login.vue';
export default {
  components: { Login },
  name: "Navbar",
  data() {
    return {
      loginStatus: false,
      username: "",
      isAdmin: this.$session.has("admin"),
      keyword: "",
      showModal : false
    };
  },
  created() {
    let status = this.$session.has("user");
    this.showModal = true
    // console.log(status);
    if (status) {
      this.loginStatus = true;
      this.username = this.$session.get("user");
    } else if (this.$session.has("admin")) {
      this.loginStatus = true;
      this.username = this.$session.get("admin");
    } else {
      this.loginStatus = false;
    }
  },
  methods: {
    toLogin: function () {
      this.showModal = true
    },
    logout: function () {
      this.$session.destroy();
      this.$router.push({
        path: "/",
      });
      this.$router.go(0)
    },
    createInvoice: function () {
      if ( this.$session.has("user") ){
        console.log("Create Invoice");
        let data = {
        cart: this.$store.getters.getCart,
        user:  this.$session.get("user"),
      };
      let options = {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      };
      fetch("http://localhost:5000/add-cart", options)
        .then((response) => {
          console.log("Create Invoice");
          return response.json();
        })
        .then((data) => {
          console.log(data);
          this.$store.commit.clearCart;
          this.$router.go(0);
          return data;
        });
      } else if ( this.$session.has("admin") ){
          this.$router.go(0)
      } else {

      }
    },
    goToCart() {
      // this.$router.push({
      //   path: "/cart",
      // });
    },
    goHome() {
      // this.$router.push({
      //   path: "/",
      // });
    },
  },
};
</script>

