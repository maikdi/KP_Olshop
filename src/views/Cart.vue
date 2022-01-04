<template>
  <div class="container-fluid">
    <!-- Start Checkout Modal -->
    <div
      class="modal fade"
      id="checkoutModal"
      tabindex="-1"
      aria-labelledby="cartSuccess"
      aria-hidden="true"
      v-if="showModal"
      @close="showModal = false"
    >
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="cartSuccess">Checkout berhasil!</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">Checkout berhasil!</div>
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
    <!-- End Checkout MODAL -->
    <Navbar class="row"></Navbar>
    <div id="cart-wrapper" class="row">
      <div id="parent-left" class="col-9 gx-3 gy-3">
        <div class="overflow-hidden p-4 border bg-light">
          <h5>Keranjang</h5>
          <button
            type="button"
            class="btn btn-outline-danger"
            @click="cancelAllItems"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-trash"
              viewBox="0 0 16 16"
            >
              <path
                d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"
              ></path>
              <path
                fill-rule="evenodd"
                d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"
              ></path>
            </svg>
            Cancel All
          </button>
          <ul class="list-group list-group-flush">
            <li
              class="list-group-item"
              v-for="(product, index) in products"
              :key="product[0]"
            >
              <div class="container">
                <div class="row row-cols-3">
                  <div class="col-1">
                    <img
                      :src="require('../assets/' + product[2])"
                      alt=""
                      style="width: 48px"
                    />
                  </div>

                  <div class="col-10">
                    <em>{{ product[0] }}</em>
                    <div class="col">
                      <b>
                        {{
                          new Intl.NumberFormat("in-IN", {
                            style: "currency",
                            currency: "IDR",
                          }).format(product[1])
                        }}
                      </b>
                    </div>
                  </div>
                  <div class="container">
                    <div class="row">
                      <div class="col-5 col-sm-1">
                        <svg
                          width="20"
                          height="20"
                          viewBox="0 0 20 20"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                          @click="minusQuantity(product[4], index)"
                        >
                          <path
                            fill-rule="evenodd"
                            clip-rule="evenodd"
                            d="M4.4443 18.3147C6.08879 19.4135 8.02219 20 10 20C12.6522 20 15.1957 18.9464 17.0711 17.0711C18.9464 15.1957 20 12.6522 20 10C20 8.02219 19.4135 6.08879 18.3147 4.4443C17.2159 2.79981 15.6541 1.51809 13.8268 0.761209C11.9996 0.00433283 9.98891 -0.193701 8.0491 0.192152C6.10929 0.578004 4.32746 1.53041 2.92894 2.92894C1.53041 4.32746 0.578004 6.10929 0.192152 8.0491C-0.1937 9.98891 0.00433283 11.9996 0.761209 13.8268C1.51809 15.6541 2.79981 17.2159 4.4443 18.3147ZM5.55544 3.34825C6.87103 2.4692 8.41775 2 10 2C12.1217 2 14.1566 2.84286 15.6569 4.34315C17.1571 5.84344 18 7.87827 18 10C18 11.5823 17.5308 13.129 16.6518 14.4446C15.7727 15.7602 14.5233 16.7855 13.0615 17.391C11.5997 17.9965 9.99113 18.155 8.43928 17.8463C6.88743 17.5376 5.46197 16.7757 4.34315 15.6569C3.22433 14.538 2.4624 13.1126 2.15372 11.5607C1.84504 10.0089 2.00347 8.40035 2.60897 6.93854C3.21447 5.47673 4.23985 4.2273 5.55544 3.34825ZM6 11H14C14.2652 11 14.5196 10.8946 14.7071 10.7071C14.8946 10.5196 15 10.2652 15 10C15 9.73478 14.8946 9.48043 14.7071 9.29289C14.5196 9.10536 14.2652 9 14 9H6C5.73478 9 5.48043 9.10536 5.29289 9.29289C5.10536 9.48043 5 9.73478 5 10C5 10.2652 5.10536 10.5196 5.29289 10.7071C5.48043 10.8946 5.73478 11 6 11Z"
                            fill="#12883D"
                          ></path>
                        </svg>
                      </div>
                      <div class="col-5 col-sm-3">
                        <input
                          :id="'input' + index"
                          type="number"
                          :value="products[index][3]"
                          class="form-control"
                          disabled
                        />
                      </div>
                      <div class="col-5 col-sm-1">
                        <svg
                          width="20"
                          height="20"
                          viewBox="0 0 20 20"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                          @click="plusQuantity(product[4], index)"
                        >
                          <path
                            fill-rule="evenodd"
                            clip-rule="evenodd"
                            d="M4.4443 18.3147C6.08879 19.4135 8.02219 20 10 20C12.6522 20 15.1957 18.9464 17.0711 17.0711C18.9464 15.1957 20 12.6522 20 10C20 8.02219 19.4135 6.08879 18.3147 4.4443C17.2159 2.79981 15.6541 1.51809 13.8268 0.761209C11.9996 0.00433283 9.98891 -0.193701 8.0491 0.192152C6.10929 0.578004 4.32746 1.53041 2.92894 2.92894C1.53041 4.32746 0.578004 6.10929 0.192152 8.0491C-0.1937 9.98891 0.00433283 11.9996 0.761209 13.8268C1.51809 15.6541 2.79981 17.2159 4.4443 18.3147ZM5.55544 3.34825C6.87103 2.4692 8.41775 2 10 2C12.1217 2 14.1566 2.84286 15.6569 4.34315C17.1571 5.84344 18 7.87827 18 10C18 11.5823 17.5308 13.129 16.6518 14.4446C15.7727 15.7602 14.5233 16.7855 13.0615 17.391C11.5997 17.9965 9.99113 18.155 8.43928 17.8463C6.88743 17.5376 5.46197 16.7757 4.34315 15.6569C3.22433 14.538 2.4624 13.1126 2.15372 11.5607C1.84504 10.0089 2.00347 8.40035 2.60897 6.93854C3.21447 5.47673 4.23985 4.2273 5.55544 3.34825ZM11 9H14C14.2652 9 14.5196 9.10536 14.7071 9.29289C14.8946 9.48043 15 9.73478 15 10C15 10.2652 14.8946 10.5196 14.7071 10.7071C14.5196 10.8946 14.2652 11 14 11H11V14C11 14.2652 10.8946 14.5196 10.7071 14.7071C10.5196 14.8946 10.2652 15 10 15C9.73478 15 9.48043 14.8946 9.29289 14.7071C9.10536 14.5196 9 14.2652 9 14V11H6C5.73478 11 5.48043 10.8946 5.29289 10.7071C5.10536 10.5196 5 10.2652 5 10C5 9.73478 5.10536 9.48043 5.29289 9.29289C5.48043 9.10536 5.73478 9 6 9H9V6C9 5.73478 9.10536 5.48043 9.29289 5.29289C9.48043 5.10536 9.73478 5 10 5C10.2652 5 10.5196 5.10536 10.7071 5.29289C10.8946 5.48043 11 5.73478 11 6V9Z"
                            fill="#12883D"
                          ></path>
                        </svg>
                      </div>
                    </div>
                  </div>
                  <div class="col-1">
                    <button
                      type="button"
                      class="btn btn-sm btn-danger float-end"
                      @click="cancelItem(product[4], index)"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="16"
                        height="16"
                        fill="currentColor"
                        class="bi bi-trash"
                        viewBox="0 0 16 16"
                      >
                        <path
                          d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"
                        />
                        <path
                          fill-rule="evenodd"
                          d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"
                        />
                      </svg>
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
            <small id="total"></small>
          </div>
          <div class="row centered">
            <button
              type="button"
              class="btn btn-success"
              @click="checkout"
              data-bs-toggle="modal"
              data-bs-target="#checkoutModal"
              v-if="products.length > 0"
            >
              Checkout
            </button>
            <button type="button" class="btn btn-success" v-else disabled>
              Checkout
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
export default {
  name: "Cart",
  data() {
    return {
      products: [],
      showModal: true,
    };
  },
  computed: {},

  created() {
    let data = {
      user: this.$session.get("user"),
    };
    let options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    };
    fetch("http://localhost:5000/get-cart", options)
      .then((response) => {
        // console.log(response);
        return response.json();
      })
      .then((data) => {
        this.products = data.data;
        this.calculateTotal();
        console.log(this.products);
      });
  },
  methods: {
    calculateTotal() {
      let amount = 0;
      this.products.forEach((product) => {
        amount += product[1] * product[3];
      });
      let total = new Intl.NumberFormat("in-IN", {
        style: "currency",
        currency: "IDR",
      }).format(amount);
      document.getElementById("total").innerHTML = total;
      return amount;
    },
    addToCart(product) {
      console.log(product);
      this.$store.commit("addProductToCart", product);
    },
    cancelItem(product_id, index) {
      let data = {
        user: this.$session.get("user"),
        product_id: product_id,
      };
      let options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      };
      fetch("http://localhost:5000/cancel-item", options)
        .then((response) => {
          // console.log(response);
          return response.json();
        })
        .then((data) => {
          this.products.splice(index, 1);
          this.calculateTotal();
          return data;
        });
    },
    minusQuantity(product_id, index) {
      if (this.products[index][3] > 1) {
        let data = {
          user: this.$session.get("user"),
          product_id: product_id,
        };
        let options = {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        };
        fetch("http://localhost:5000/minus-quantity", options)
          .then((response) => {
            // console.log(response);
            return response.json();
          })
          .then((data) => {
            this.products[index][3] -= 1;
            document.getElementById("input" + index).value =
              this.products[index][3];
            console.log(this.products[index]);
            this.calculateTotal();

            return data;
          });
      }
    },
    plusQuantity(product_id, index) {
      let data = {
        user: this.$session.get("user"),
        product_id: product_id,
      };
      let options = {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      };
      fetch("http://localhost:5000/plus-quantity", options)
        .then((response) => {
          // console.log(response);
          return response.json();
        })
        .then((data) => {
          this.products[index][3] += 1;
          document.getElementById("input" + index).value =
            this.products[index][3];
          console.log(this.products[index]);
          this.calculateTotal();
          return data;
        });
    },
    async checkout() {
      if (this.$session.has("user")) {
        if (this.products.length > 0) {
          this.showModal = true;
          await sleep(2000);
          var today = new Date();
          var date =
            today.getFullYear() +
            "-" +
            (today.getMonth() + 1) +
            "-" +
            today.getDate();
          var time =
            today.getHours() +
            ":" +
            today.getMinutes() +
            ":" +
            today.getSeconds();
          var dateTime = date + " " + time;
          let total = this.calculateTotal();
          console.log(total);
          let data = {
            user: this.$session.get("user"),
            total: total,
            date: dateTime,
          };
          let options = {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
          };
          fetch("http://localhost:5000/checkout", options)
            .then((response) => {
              // console.log(response);
              return response.json();
            })
            .then((data) => {
              let email_data = {
                subject: "Incoming Invoice",
                to: this.$session.get("user") ,
                body: "Pesanan masuk !",
              };
              let email_options = {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify(email_data),
              };
              fetch("http://localhost:5000/send_mail", email_options)
                .then((response) => {
                  // console.log(response);
                  return response.json();
                })
                .then((data) => {
                  
                });
                this.showModal = false;
                  this.$router.push({
                    path: "/",
                  });
                  this.$router.go(0);
            });
        } else {
          this.$router.push({
            path: "/login",
          });
        }
      } else {
      }
    },
    cancelAllItems() {
      let data = {
        user: this.$session.get("user"),
      };
      let options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      };
      fetch("http://localhost:5000/cancel-all", options)
        .then((response) => {
          // console.log(response);
          return response.json();
        })
        .then((data) => {
          this.products = [];
          this.calculateTotal();
          return data;
        });
    },
  },
};
</script>