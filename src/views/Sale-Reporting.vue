<template>
  <div>
    <Navbar></Navbar>
    <div>
      <form class="row row-cols-lg-auto g-3 align-items-center">
        <label for="start-date">Tgl: </label>
        <input type="date" id="start-date" name="start-date" />
        <label for="end-date">sampai </label>
        <input type="date" id="end-date" name="end-date" />
        <div class="col-12">
          <button type="submit" class="btn btn-outline-primary">Search</button>
        </div>
        <div class="form-check">
          <input
            class="form-check-input"
            type="checkbox"
            value=""
            id="flexCheckDefault"
          />
          <label class="form-check-label" for="flexCheckDefault">
            By Product Only
          </label>
        </div>
      </form>
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
              <th>Nama</th>
              <th>Harga</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td>1</td>
              <td>Iphone XXX_cH41215_hUlU_XXX</td>
              <td>Rp. 1.000.000</td>
            </tr>
          </tbody>
		  <tfoot>
			  <tr>
				<td colspan="2"></td>
				<td><b>Total</b></td>
			  </tr>
 		 </tfoot>
        </table>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* * {
	padding: 0;
} */
form {
  margin: auto;
}
</style>