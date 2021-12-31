<template>
  <div class="container-fluid">
    <svg xmlns="http://www.w3.org/2000/svg" style="display: none">
      <symbol
        id="exclamation-triangle-fill"
        fill="currentColor"
        viewBox="0 0 16 16"
      >
        <path
          d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"
        />
      </symbol>
    </svg>
    <div class="card container pb-3" style="width: 500px">
    <h3 class="card-header text-center">Login</h3>
    <div id="card-body">
      <div v-if="valid==false" class="row">
        <div class="alert alert-danger d-flex align-items-center" role="alert">
          <svg
            class="bi flex-shrink-0 me-2"
            width="24"
            height="24"
            role="img"
            aria-label="Danger:"
          >
            <use xlink:href="#exclamation-triangle-fill" />
          </svg>
          <div>Username/Password tidak ditemukan</div>
        </div>
      </div>

      <div class="mb-6 mt-2">
        <label for="username" class="form-label">Username</label>
        <input
          type="text"
          class="form-control"
          id="username"
          v-model="credentials.username"
        />
      </div>

      <div class="mb-6 mt-2">
        <label for="password" class="form-label">Password</label>
        <input
          type="password"
          class="form-control"
          id="password"
          v-model="credentials.password"
        />
      </div>

      <div class="mb-6 mt-4 text-center">
        <button class="btn btn-primary" @click="checkLogin">Login</button>
      </div>

      <div class="d-flex justify-content-center mt-3">
        <div class="small d-inline text-center" style="margin-right: 3px">Don't have an account?</div>
        <a href="#/sign-up" class="small d-inline text-center text-decoration-none">
          <b>Sign Up</b>
        </a>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      credentials: {
        username: "",
        password: "",
      },
      valid: true,
    };
  },
  methods: {
    checkLogin() {
      let options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.credentials),
      };
      console.log(this.credentials);
      fetch("http://localhost:5000/login", options)
      .then((response) => {
        console.log(response);
        return response.json();
      }).then((data) => {
        if (data.response == "User"){
          this.$session.set("user",this.credentials.username)
          this.$emit("valid")
        }
        else if (data.response == "Not Valid"){
          this.valid = false
        } 
        else if (data.response == "Admin"){
          this.$session.set("admin",this.credentials.username)
          this.$emit("valid")
          
        }
      })
    }
  }
}

</script>

<style scoped>
.login {
  display: grid;
  place-items: center;
  min-height: 100vh;
}
</style>
