<script>
	export default {
		globalData:{
			uid : -1,
			urlRoot: "http://127.0.0.1:5000/",
		},
		onLaunch: function() {
			console.log('App Launch')
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style>
	/*每个页面公共css */
	page{
		background-color: #eef7fe;
	}
</style>
