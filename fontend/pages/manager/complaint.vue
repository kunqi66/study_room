<template>
	<view>
		<view class="uni-container">
			<uni-table ref="com_table" border stripe emptyText="暂无更多数据">
							<uni-tr>
								<uni-th width="70" align="center">教室号</uni-th>
								<uni-th width="70" align="center">座位号</uni-th>
								<uni-th width="70" align="center">日期</uni-th>
								<uni-th width="200" align="center">原因</uni-th>
								<uni-th width="200" align="center">选项</uni-th>
								<uni-th width="180" align="center"></uni-th>
							</uni-tr>
							<uni-tr v-for="(item, index) in table_data" :key="index">
								<uni-td align="center" class="td">{{ table_data[index].class_number }}</uni-td>
								<uni-td align="center" class="td">{{ table_data[index].number }}</uni-td>
								<uni-td align="center" class="td">{{ table_data[index].date }}</uni-td>
								<uni-td align="center" class="td">{{ table_data[index].reason }}</uni-td>
								<uni-td>
									<view class="uni-group">
										<button class="uni-button" size="mini" type="primary" v-if="table_data[index].result=='W'" @click="pz(index,'A')">批准</button>
										<button class="uni-button" size="mini" type="warn" v-if="table_data[index].result=='W'" @click="pz(index,'E')" >驳回</button>
										<uni-title type="h2" title="已批准" color="#ffaaa7" v-if="table_data[index].result=='A'" ></uni-title>
										<uni-title type="h2" title="已驳回" color="#ffaaa7" v-if="table_data[index].result=='E'" ></uni-title>
									</view>
								</uni-td>
							</uni-tr>
			</uni-table>
			<view class="uni-pagination-box"><uni-pagination show-icon :page-size="pageSize" :current="pageCurrent" :total="total" @change="change" /></view>
		</view>	
	</view>
</template>

<script>
	export default {
		data() {
			return {
				table_data:[
				],
				deal:1,
			}
		},
		onLoad() {
			var that=this
			 uni.request({
			 	header: {
			 	   'content-type':'application/x-www-form-urlencoded'},
			 	url:getApp().globalData.urlRoot+"manager/loadComp",
			 	method:'POST',
			 	data:{
					
			 	},
			 	success: (res) => {
			 		that.table_data=res.data.form
					console.log(that.table_data[0].result)
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
			pz(index,result){
				var that=this;
				uni.request({
					url:getApp().globalData.urlRoot+"manager/dealComp",
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					data:{
						"id":index+1,
						"result":result,
					},       //json
					method:"POST",
					success(res) {
						if(res.data.suc){
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty'
							})
						}else{
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty',
								duration:1500,
							})
						}
					}
				})
			},
		}
	}
</script>

<style>
	.uni-group{
		text-align: center;
	}
	.uni-button{
		margin-top: 5px;
		margin-left: 5px;
	}
</style>
