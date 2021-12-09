<template>
  <div class="login">
  <form>
  <div class="mb-6">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-6">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-6">
          <router-link to="/welcome"><button class="btn btn-primary" type="submit">Login</button>
</router-link>
  </div>
</form>
  </div>
</template>

<script>
import { defineComponent } from '@vue/composition-api'

export default defineComponent({
  setup() {
    
  },
})
</script>

<style scoped>
.login {
display: grid;
place-items: center;
min-height: 100vh;
}
form{
padding: 20px;
box-shadow: 5px 5px 5px 5px #888888;
}
</style>
