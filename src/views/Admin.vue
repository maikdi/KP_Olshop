<template>
  <div>
    <Navbar></Navbar>
    <form class="row row-cols-lg-auto g-3 align-items-center">
      <div class="col-12">
        <label class="visually-hidden" for="inlineFormInputGroupSearch"
          >Search</label
        >
        <div class="input-group">
          <div class="input-group-text">Keyword:</div>
          <input
            type="text"
            class="form-control"
            id="inlineFormInputGroupSearch"
          />
        </div>
      </div>
      <div class="col-12">
        <button type="submit" class="btn btn-outline-primary">Search</button>
      </div>
    </form>
    <div style="margin: 10px">
      <button type="button" class="btn btn-primary btn-lg">+ Add Items</button>
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