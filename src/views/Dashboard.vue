<template>
  <div class="container-fluid">
    <!-- Modal -->
    <div
      class="modal fade"
      id="exampleModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
      v-if="showModal" @close="showModal = false"
    >
      <div class="modal-dialog modal-dialog-centered">
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
                <img :src="require('../assets/' + details[5])" alt="" style="width:240px;">
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
                <br>
                <p>Kategori: {{details[3]}}</p>
                <p>
                  Deskripsi:
                </p>
                <br>
                <p>
                  {{details[4]}}
                </p>
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
            <button type="button" class="btn btn-success" data-bs-dismiss="modal">Add to cart</button>
          </div>
        </div>
      </div>
    </div>
    <!-- END MODAL -->
    <Navbar class="row"></Navbar>
    <div class="row row-cols-4 row-cols-md-4 g-4">
      <div class="col" v-for="product in products" :key="product[0]">
        <div class="card" style="width: 18rem; margin-top: 10px">
          <img :src="require('../assets/' + product[5])" class="card-img-top" />
          <div class="card-body">
            <p class="card-title">
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
            <a
              href="#"
              class="btn btn-primary"
              data-bs-toggle="modal"
              data-bs-target="#exampleModal"
              v-on:click="toggleModal(product[0] - 1)"
              >Details</a 
            >
            <a href="#" class="btn btn-success">Add to cart</a>
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
      showModal: false
    };
  },
  created() {
    fetch("http://localhost:5000/get_dashboard")
      .then((response) => {
        // console.log(response);
        return response.json();
      })
      .then((data) => {
        this.products = data.data;
        this.$store.commit('setProducts', data.data)
        // console.log(data);
        this.toggleModal(0);
      });
  },
  methods: {
    toggleModal(index) {
      this.details = this.$store.getters.productDetails(index);
      this.showModal = true
      console.log(this.details);
    }
  },
};
</script>