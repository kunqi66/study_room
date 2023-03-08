<template>
	<view>
		<uni-table ref="table" :loading="loading" border stripe type="selection" emptyText="暂无更多数据" @selection-change="selectionChange">
			<uni-tr>
				<uni-th width="100" aling="center">姓名</uni-th>
				<uni-th width="100" aling="center">学号</uni-th>
				<uni-th width="100" aling="center">电话</uni-th>
				<uni-th width="80" align="center">设置</uni-th>
			</uni-tr>
			<uni-tr v-for="(item,index) in editUser" :key="index">
				<uni-td align="center">{{ editUser[index].name }}</uni-td>
				<uni-td align="center">{{ editUser[index].student_number }}</uni-td>
				<uni-td align="center">{{ editUser[index].number }}</uni-td>
				<uni-td>
					<button class="uni-button" v-if="item.illegal_number<=15" size="mini" type="primary">可用</button>
					<button v-else>不可用</button>
				</uni-td>
				<uni-td>
					<view class="uni-group">
						<button class="uni-button" size="mini" type="primary">修改</button>
					</view>
				</uni-td>
			</uni-tr>
		</uni-table>
		<view class="uni-pagination-box"><uni-pagination show-icon :page-size="pageSize" :current="pageCurrent" :total="total" @change="change" /></view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				editUser:[],
				searchVal: '',
				// 每页数据量
				pageSize: 10,
				// 当前页
				pageCurrent: 1,
				// 数据总量
				total: 0,
				loading: false
			}
		},
		onLoad() {
			this.selectedIndexs = []
			this.getData(1)
			var that=this
			uni.request({
				header: {'Authorization':getApp().globalData.token,
				   'content-type':'application/x-www-form-urlencoded'},
				url:getApp().globalData.urlRoot+"manager/Loadmanager",
				method:'POST',
				data:{
					uid:-1,
				},
				success: (res) => {
					if(res.data.suc){
						console.log("获取用户列表成功")
						that.editUser=res.data.form
						console.log(that.editUser[0].name)
						console.log(res.data.form)
					}else{
						console.log("未查询到数据")
						console.log(res.data.message)
					}
				},
				fail() {
					uni.showToast({
						title: "获取失败！",
						icon: 'none'
					})
				}
			})
			},
		methods: {

		}
	}
</script>

<style>

</style>