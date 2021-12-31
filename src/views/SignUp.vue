<template>
  <div class="sign-up">
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
    <div class="card container" style="width: 500px">
      <h3 class="card-header text-center">Sign Up</h3>
      <div class="card-body">
        <form>
          <div v-if="status == 1">
            <div
              class="alert alert-warning d-flex align-items-center"
              role="alert"
            >
              <svg
                class="bi flex-shrink-0 me-2"
                width="24"
                height="24"
                role="img"
                aria-label="Warning:"
              >
                <use xlink:href="#exclamation-triangle-fill" />
              </svg>
              <div>
                This username is already taken. Please choose another username.
              </div>
            </div>
          </div>
          <div v-if="status == 2 || status == 3">
            <div
              class="alert alert-warning d-flex align-items-center"
              role="alert"
            >
              <svg
                class="bi flex-shrink-0 me-2"
                width="24"
                height="24"
                role="img"
                aria-label="Warning:"
              >
                <use xlink:href="#exclamation-triangle-fill" />
              </svg>
              <div>Please choose a username.</div>
            </div>
          </div>
          <div v-if="status == 2 || status == 4">
            <div
              class="alert alert-warning d-flex align-items-center"
              role="alert"
            >
              <svg
                class="bi flex-shrink-0 me-2"
                width="24"
                height="24"
                role="img"
                aria-label="Warning:"
              >
                <use xlink:href="#exclamation-triangle-fill" />
              </svg>
              <div>Please choose a password.</div>
            </div>
          </div>
          <div class="row">
            <div class="form-group col-md-6">
              <label class="form-label">First Name</label>
              <input
                type="text"
                class="form-control"
                v-model="credentials.first_name"
              />
            </div>
            <div class="form-group col-md-6">
              <label class="form-label">Last Name</label>
              <input
                type="text"
                class="form-control"
                v-model="credentials.last_name"
              />
            </div>
          </div>

          <div class="form-group mt-2">
            <label class="form-label">Username</label>
            <input
              type="text"
              class="form-control"
              v-model="credentials.username"
            />
            <div class="invalid-feedback">Please choose a username.</div>
          </div>
          <div class="mt-2">
            <label class="form-label">Email</label>
            <input
              type="password"
              class="form-control"
              v-model="credentials.email"
            />
          </div>
          <div class="mt-2">
            <label class="form-label">Password</label>
            <input
              type="password"
              class="form-control"
              v-model="credentials.password"
            />
          </div>

          <div class="text-center mt-4">
            <button class="btn btn-primary" @click="signUp">Sign Up</button>
          </div>

          <div class="d-flex justify-content-center mt-3">
            <div class="small d-inline text-center" style="margin-right: 3px">Have an account?</div>
            <router-link to='/login' class="small d-inline text-center text-decoration-none">
              <b>Sign In</b>
            </router-link>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Registration",
  data() {
    return {
      credentials: {
        first_name: "",
        last_name: "",
        username: "",
        password: "",
        email: ""
      },
      status: null,
    };
  },
  methods: {
    signUp() {
      let options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.credentials),
      };
      fetch("http://localhost:5000/sign-up", options)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data);
          if (data.response == "valid") {
            alert("Registration Success!");
            this.$router.push({
              path: "/",
            });
          } else if (data.response == "username taken") {
            this.status = 1;
          } else if (data.response == "required field") {
            this.status = 2;
          } else if (data.response == "username blank") {
            this.status = 3;
          } else if (data.response == "password blank") {
            this.status = 4;
          }
        });
    },
  },
};
</script>

<style scoped>
.sign-up {
  display: grid;
  place-items: center;
  min-height: 100vh;
}
</style>