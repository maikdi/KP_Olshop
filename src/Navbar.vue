<template>
  <div class="justify-content-center">
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
          <a class="nav-link active" aria-current="page" href="#/" @click="goHome">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#/cart" @click="createInvoice">Keranjang</a>
        </li>
        </ul>
      </div>
      <!-- DIV FOR SEARCH BAR ONLY -->
      <div class="container-fluid">
        <form class="d-flex">
          <input
            class="form-control me-2 col-auto"
            type="search"
            placeholder="Search"
            aria-label="Search"
          />
          <button class="btn btn-outline-light" type="submit">Search</button>
        </form>
      </div>
      <!-- DIV FOR USER SECTION -->
      <div class="container-fluid"></div>
      <div class="d-flex" v-if="loginStatus">
          <a class="btn btn-outline-light me-2 col-auto" aria-current="page">
            {{ this.username }}
          </a>
          <a class="btn btn-outline-light" aria-current="page" @click="logout"> Logout </a>
      </div>
      <div v-else>
          <a class="btn btn-outline-light" aria-current="page" @click="toLogin">
            Login
          </a>
        </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      loginStatus: false,
      username: "",
    };
  },
  created() {
    let status = this.$session.has("user");
    // console.log(status);
    if (status) {
      this.loginStatus = true;
      this.username = this.$session.get("user");
    }
    else if (this.$session.has("admin")){
      this.loginStatus = true;
      this.username = this.$session.get("admin");
    } else {
      this.loginStatus = false;
    }
  },
  methods: {
    toLogin: function () {
      this.$router.push({
        path: "/login",
      });
    },
    logout: function() {
      this.$session.clear()
      this.$router.go(0)
      this.$router.push({
        path: "/",
      });
    },
    createInvoice: function() {
      let data = {
        cart : this.$store.getters.getCart,
        user : this.username
        }
      let options = {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      };
      fetch("http://localhost:5000/add-cart", options)
      .then((response) => {
        return response
      }).then((data)=> {
        console.log(data);
        this.$store.commit.clearCart
        return data
      })  
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
    }
  },
};
</script>

