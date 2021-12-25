<template>
  <div class="welcome">
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
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
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
      <div class="container-fluid">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page">
              {{this.username}}
            </a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Welcome",
  data() {
    return {
      username: this.$session.get("user"),
    };
  },
};
</script>

<style scoped>
nav {
  justify-content: space-between;
}
</style>
