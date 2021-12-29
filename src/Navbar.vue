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
          <button class="btn btn-outline-light col-auto" type="submit" @click="$emit('search', keyword)"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
  <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
</svg> Search</button>
      </div>
      <!-- DIV FOR USER SECTION -->
      <div class="container-fluid"></div>
      <div class="container-fluid justify-content-end" v-if="loginStatus"><div class="row row-cols-auto">
        <div class="col"><a class="btn btn-outline-light me-2" aria-current="page">
          {{ this.username }}
        </a></div>
        <div class="col"><a class="btn btn-outline-light" aria-current="page" @click="logout"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-box-arrow-left" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0v2z"/>
  <path fill-rule="evenodd" d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z"/>
</svg>
           Logout
        </a></div>
    
      </div></div>
      
      <div class="col-auto" v-else>
        <a class="btn btn-outline-light" aria-current="page" @click="toLogin" data-bs-toggle="modal" data-bs-target="#loginModal">
         <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-door-open" viewBox="0 0 16 16">
  <path d="M8.5 10c-.276 0-.5-.448-.5-1s.224-1 .5-1 .5.448.5 1-.224 1-.5 1z"></path>
  <path d="M10.828.122A.5.5 0 0 1 11 .5V1h.5A1.5 1.5 0 0 1 13 2.5V15h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V1.5a.5.5 0 0 1 .43-.495l7-1a.5.5 0 0 1 .398.117zM11.5 2H11v13h1V2.5a.5.5 0 0 0-.5-.5zM4 1.934V15h6V1.077l-6 .857z"></path>
</svg> Login
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

