<template>
  <div>
    <!-- Start Details Modal -->
    <div
      class="modal fade"
      id="editModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
      v-if="showModal"
      @close="showModal = false"
    >
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Edit Product</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div class="row">
              <div class="mb-3">
                <label for="formFile" class="form-label">Gambar baru: </label>
                <input
                  class="form-control"
                  type="file"
                  id="upload"
                  accept=".jpg, .jpeg, .png"
                />
              </div>
              <div class="col">
                <label for="newName">Nama baru:</label>
                <textarea
                  name="newName"
                  id="newName"
                  cols="30"
                  rows="1"
                  v-model="details[1]"
                  class="form-control"
                ></textarea
                ><br />
                <label for="newPrice">Harga baru:</label>
                <textarea
                  name="newName"
                  id="newName"
                  cols="30"
                  rows="1"
                  v-model="details[2]"
                  class="form-control"
                ></textarea>
                <br />
                <label for="newCat">Kategori baru:</label>
                <textarea
                  name="newCat"
                  id="newCat"
                  cols="30"
                  rows="1"
                  v-model="details[3]"
                  class="form-control"
                ></textarea>
                <br />
                <label for="newDesc">Deskripsi baru:</label>
                <textarea
                  name="newDesc"
                  id="newDesc"
                  cols="30"
                  rows="1"
                  v-model="details[4]"
                  class="form-control"
                ></textarea>
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
            <button
              type="button"
              class="btn btn-success"
              @click="saveProduct()"
              data-bs-dismiss="modal"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-check-circle-fill"
                viewBox="0 0 16 16"
              >
                <path
                  d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"
                ></path>
              </svg>
              Save
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- End Details MODAL -->
    <!-- Start New Product Modal -->
    <div
      class="modal fade"
      id="addModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
      v-if="showModal"
      @close="showModal = false"
    >
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Add New Product</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div class="row">
              <div class="mb-3">
                <label for="formFile" class="form-label">Gambar baru: </label>
                <input
                  class="form-control"
                  type="file"
                  id="newImage"
                  accept=".jpg, .jpeg, .png"
                  required
                />
              </div>
              <div class="col">
                <label for="newName">Nama baru:</label>
                <textarea
                  name="newName"
                  id="newName"
                  cols="30"
                  rows="1"
                  v-model="newProduct.name"
                  class="form-control"
                ></textarea
                ><br />
                <label for="newPrice">Harga baru:</label>
                <textarea
                  name="newName"
                  id="newName"
                  cols="30"
                  rows="1"
                  v-model="newProduct.price"
                  class="form-control"
                ></textarea>
                <br />
                <label for="newCat">Kategori baru:</label>
                <textarea
                  name="newCat"
                  id="newCat"
                  cols="30"
                  rows="1"
                  v-model="newProduct.details"
                  class="form-control"
                ></textarea>
                <br />
                <label for="newDesc">Deskripsi baru:</label>
                <textarea
                  name="newDesc"
                  id="newDesc"
                  cols="30"
                  rows="1"
                  v-model="newProduct.description"
                  class="form-control"
                ></textarea>
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
            <button
              type="button"
              class="btn btn-success"
              @click="addProduct"
              data-bs-dismiss="modal"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-check-circle-fill"
                viewBox="0 0 16 16"
              >
                <path
                  d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"
                ></path>
              </svg>
              Save
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- End New Product MODAL -->
    <Navbar></Navbar>
    <div class="container-fluid" style="margin-top: 10px">
      <div class="row row-cols-auto">
        <div class="col-2">
          <div class="input-group">
            <div class="input-group-text">Keyword:</div>
            <input
              type="text"
              class="form-control"
              id="inlineFormInputGroupSearch"
              v-model="keyword"
            />
          </div>
        </div>
        <div class="col-2">
          <button type="submit" class="btn btn-outline-primary col-auto" @click="search"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
  <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
</svg>
            Search
          </button>
        </div>
      </div>
    </div>

    <div style="margin: 10px">
      <button
        type="button"
        class="btn btn-primary btn-lg"
        data-bs-toggle="modal"
        data-bs-target="#addModal"
        @click="showModal = true"
      >
        + Add Product
      </button>
    </div>
    <div class="row" style="margin: 10px">
      <div class="col-md-12">
        <table class="table table-bordered">
          <caption>
            Viewing 1 of 1 Item(s)
          </caption>
          <thead>
            <tr>
              <th>No.</th>
              <th>Id</th>
              <th></th>
              <!-- Placeholder for image -->
              <th>Nama</th>
              <th>Harga</th>
              <th>Description</th>
              <th></th>
              <!-- Placeholder for Edit -->
              <th></th>
              <!-- Placeholder for Delete Product -->
            </tr>
          </thead>
          <tbody>
            <tr v-for="(product, index) in products" :key="product[0]">
              <td style="width: 50px">{{ index + 1 }}</td>
              <td style="width: 50px">{{ product[0] }}</td>
              <td style="width: 100px" :id="'image' + product[0]">
                <img
                  :src="require('../assets/' + product[5])"
                  class="card-img-top"
                  style="height: 64px"
                />
              </td>
              <td>
                <p
                  :id="'name' + product[0]"
                  style="
                    overflow: hidden;
                    text-overflow: ellipsis;
                    display: -webkit-box;
                    -webkit-line-clamp: 1;
                    line-clamp: 1;
                    -webkit-box-orient: vertical;
                  "
                >
                  {{ product[1] }}
                </p>
              </td>
              <td :id="'price' + product[0]" style="width: 100px">
                {{
                  new Intl.NumberFormat("in-IN", {
                    style: "currency",
                    currency: "IDR",
                  }).format(product[2])
                }}
              </td>
              <td style="width: 600px">
                <p
                  :id="'desc' + product[0]"
                  style="
                    overflow: hidden;
                    text-overflow: ellipsis;
                    display: -webkit-box;
                    -webkit-line-clamp: 1;
                    line-clamp: 1;
                    -webkit-box-orient: vertical;
                  "
                >
                  {{ product[4] }}
                </p>
              </td>
              <td>
                <button
                  type="button"
                  class="btn btn-secondary"
                  data-bs-toggle="modal"
                  data-bs-target="#editModal"
                  @click="editProduct(index)"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-pencil"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z"
                    ></path>
                  </svg>
                  Edit
                </button>
              </td>
              <!-- Placeholder for Edit -->
              <td>
                <button
                  type="button"
                  class="btn btn-danger"
                  @click="deleteProduct(index)"
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
                  Remove
                </button>
              </td>
              <!-- Placeholder for Delete -->
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Administration",
  data() {
    return {
      products: [],
      details: [],
      showModal: false,
      newProduct: {
        name: "",
        price: 0,
        category: "",
        description: "",
        image_name: "",
      },
      editedIndex: 0,
      keyword: "",
    };
  },
  methods: {
    editProduct(index) {
      this.details = this.$store.getters.productDetails(index);
      this.showModal = true;
      this.editedIndex = index;
    },
    search() {
      let options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.keyword),
      };
      fetch("http://localhost:5000/search-product", options)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data);
          this.products = data.data;
        });
    },
    addProduct() {
      var fileInput = document.getElementById("newImage");
      let uploaded_img = fileInput.files[0];
      var formData = new FormData();
      if (uploaded_img != undefined) {
        console.log(uploaded_img);
        var filename = fileInput.files[0].name;
        this.newProduct.image_name = filename;
        formData.append("image_file", uploaded_img);
      } else {
        formData = "";
      }
      let data = this.newProduct;
      let options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      };
      let image_options = {
        method: "POST",
        body: formData,
      };
      fetch("http://localhost:5000/add-product", options)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          fetch("http://localhost:5000/update-image", image_options)
            .then((response) => {
              return response.json();
            })
            .then((data) => {
              let email_data = {
                subject: "Produk Baru",
                to: "all",
                body: "Pengguna, ada sebuah produk baru. Silahkan dilihat!",
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
              this.$router.go(0);       
            });
        });
    },
    deleteProduct(index) {
      var product_id = this.products[index][0];
      console.log(this.products);
      console.log(product_id);
      this.products.splice(index, 1);
      let data = {
        data: product_id,
      };
      let options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      };
      fetch("http://localhost:5000/delete-product", options);
    },
    saveProduct() {
      var fileInput = document.getElementById("upload");
      let uploaded_img = fileInput.files[0];
      var formData = new FormData();
      if (uploaded_img != undefined) {
        console.log(uploaded_img);
        var filename = fileInput.files[0].name;
        this.details[5] = filename;
        formData.append("image_file", uploaded_img);
      } else {
        formData = "";
      }
      this.products[this.editedIndex] = this.details;
      console.log(formData);
      let data = {
        data: this.details,
      };
      let options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      };
      let image_options = {
        method: "POST",
        body: formData,
      };
      fetch("http://localhost:5000/update-product", options)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          fetch("http://localhost:5000/update-image", image_options)
            .then((response) => {
              return response;
            })
            .then((data) => {
              this.$router.go(0);
            });
        });
    },
  },
  created() {
    fetch("http://localhost:5000/get_dashboard")
      .then((response) => {
        // console.log(response);
        return response.json();
      })
      .then((data) => {
        this.products = data.data;
        this.$store.commit("setProducts", data.data);
        this.editProduct(0);
        // console.log(data);
      });
  },
};
</script>

<style scoped>
/* * {
	padding: 0;
} */
form {
  margin: auto;
}
</style>