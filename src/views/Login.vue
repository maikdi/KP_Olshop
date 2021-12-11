<template>
  <div class="login">
    <div id="form">
      <div class="mb-6">
        <label for="username" class="form-label">Username</label>
        <input type="text" class="form-control" id="username" v-model="credentials.username">
      </div>
      <div class="mb-6">
        <label for="password" class="form-label">Password</label>
        <input type="password" class="form-control" id="password" v-model="credentials.password">
      </div>
      <div class="mb-6">
        <button class="btn btn-primary" @click="checkLogin">Login</button>
      </div>
    </div>
  </div>
</template>

<script>
export default ({
  name: "Login",
  data() {  
    return {
      credentials : {
        username: "",
        password: ""
      }
    }
  },
  methods: {
    checkLogin() {
      let options = {
        method : "POST",
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.credentials)
      }
      console.log(this.credentials);
      fetch("http://localhost:5000/login", options)
      .then((response) => {
        console.log(response);
        return response.json();
      }).then((data) => {
        if (data.response == "Valid"){
          this.$router.push({
                path: '/welcome'
            })
        }
        else if (data.response == "Not Valid"){
          this.$router.push({
                path: '/'
            })
        }
      })
    }
  },
})
</script>

<style scoped>
.login {
  display: grid;
  place-items: center;
  min-height: 100vh;
}
#form{
  padding: 20px;
  box-shadow: 5px 5px 5px 5px #888888;
}
</style>
