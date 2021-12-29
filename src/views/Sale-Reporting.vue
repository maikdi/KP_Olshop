<template>
  <div>
    <Navbar></Navbar>
    <div class="container-fluid" style="margin-top:10px">
      <div class="row row-cols-auto">
        <div class="col">
          <label for="start-date" class="col-form-label">Tgl: </label>
        </div>
        <div class="col"><input
          type="date"
          id="start-date"
          name="start-date"
          class="form-control"
          v-model="startDate"
        /></div>
        
        <div class="col"><label for="end-date" class="col-form-label">sampai </label></div>
        <div class="col"><input type="date" id="end-date" name="end-date" class="form-control" v-model="endDate" />
        </div>
        <div class="col"></div>
          <button type="submit" class="btn btn-outline-primary col-auto" @click="search"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
  <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
</svg> Search</button>
        </div>
      <div class="row row-cols-auto">
        <div class="col">
          <label class="form-check-label" for="flexCheckDefault">
            <input
            class="form-check-input"
            type="checkbox"
            v-model="checked"
            id="flexCheckDefault"
          />
            By Product Only
          </label>
        </div>
      </div>
    </div>
    <div class="row" style="margin: 10px">
      <div class="col-md-12">
        <!-- Table by product only -->
        <table class="table table-bordered" v-if="checked">
          <caption>
            Viewing 1 of 1 Item(s)
          </caption>
          <thead>
            <tr>
              <th>Invoice ID</th>
              <th>Tanggal</th>
              <th>Nama Produk</th>
              <th>Kuantitas</th>
              <th>Harga per Produk</th>
              <th>Subtotal</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(sale, index) in product_sales" :key=index>
              <td>{{ sale[1] }}</td>
              <td>{{ sale[0] }}</td>
              <td>{{ sale[2] }}</td>
              <td>{{ sale[3] }}</td>
              <td>{{ new Intl.NumberFormat("in-IN", {
                      style: "currency",
                      currency: "IDR",
                    }).format(sale[4]) }}</td>
              <td>{{ new Intl.NumberFormat("in-IN", {
                      style: "currency",
                      currency: "IDR",
                    }).format(sale[3] * sale[4] )}}</td>
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <td colspan="2"></td>
              <td colspan="2"></td>
              <td class="table-active"><b>Total</b></td>
              <td class="table-active"><b>{{ calculateTotal }}</b></td>
            </tr>
          </tfoot>
        </table>
        <!-- Table by invoice only -->
        <table class="table table-bordered" v-else>
          <caption>
            Viewing 1 of 1 Item(s)
          </caption>
          <thead>
            <tr>
              <th>Sales ID</th>
              <th>Tanggal</th>
              <th>Invoice ID</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="sale in sales" :key=sale[0]>
              <td class="align-middle">{{ sale[0] }}</td>
              <td class="align-middle">{{ sale[3] }}</td>
              <td class="align-middle">{{ sale[1] }}</td>
              <td class="align-middle">{{
                    new Intl.NumberFormat("in-IN", {
                      style: "currency",
                      currency: "IDR",
                    }).format(sale[2])
                  }}</td>
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <td colspan="2"></td>
              <td class="table-active"><b>Total</b></td>
              <td class="table-active"><b>{{ calculateTotal }}</b></td>
            </tr>
          </tfoot>
        </table>
      </div>
    </div>
  </div>
</template>

<script>

export default ({
  data() {
    return {
      checked: false,
      sales: [],
      product_sales: [],
      startDate: "",
      endDate: "",
    }
  },
  methods: {
    search() {
      let data = {
        startDate : this.startDate,
        endDate : this.endDate
      }
      let options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      }
      fetch("http://localhost:5000/search-sale", options)
      .then((response) => {
        // console.log(response);
        return response.json();
      })
      .then((data) => {
        this.sales = data.all_sales;
        this.product_sales = data.all_product_sales;
        console.log(this.sales);
        // console.log(data);
      });
    }
  },
  created() {
    fetch("http://localhost:5000/get-sale-report")
      .then((response) => {
        // console.log(response);
        return response.json();
      })
      .then((data) => {
        this.sales = data.all_sales;
        this.product_sales = data.all_product_sales;
        // console.log(data);
      });
  },
  computed: {
    calculateTotal() {
      let amount = 0;
      this.sales.forEach((sale) => {
        amount += sale[2];
      });
      let total = new Intl.NumberFormat("in-IN", {
        style: "currency",
        currency: "IDR",
      }).format(amount);
      // document.getElementById("total").innerHTML = total;
      return total;
    }
  }
})
</script>

<style scoped>
/* * {
	padding: 0;
} */
form {
  margin: auto;
}
</style>