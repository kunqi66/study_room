<template>
	<view>
		<view class="uni-container">
			<uni-table ref="com_table" :loading="loading" border stripe emptyText="暂无更多数据" @selection-change="selectionChange">
							<uni-tr>
								<uni-th width="70" align="center">教室号</uni-th>
								<uni-th width="70" align="center">座位号</uni-th>
								<uni-th width="70" align="center">日期</uni-th>
								<uni-th width="200" align="center">原因</uni-th>
								<uni-th width="180" align="center"></uni-th>
							</uni-tr>
							<uni-tr v-for="(item, index) in table_data" :key="index">
								<uni-td align="center" class="td">{{ table_data[index].class_number }}</uni-td>
								<uni-td align="center" class="td">{{ table_data[index].number }}</uni-td>
								<uni-td align="center" class="td">{{ table_data[index].date }}</uni-td>
								<uni-td align="center" class="td">{{ table_data[index].reason }}</uni-td>
								<uni-td>
									<view class="uni-group">
										<button class="uni-button" size="mini" type="primary" @click="editMmanager(index)">批准</button>
										<button class="uni-button" size="mini" type="warn" @click="deleteManager(index)" >驳回</button>
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
					{
						"class_number":"21",
						"number":"21",
						"date":"32",
						"reason":"阿斯加德辣椒水开了多久拉看似简单凯乐科技阿里将大大力开始打卡会计核算代价安静客户数的卡德加"
					},
					{
						"class_number":"321",
						"number":"2",
						"date":"2",
						"reason":"舍杜画家山东矿机架势接口回调对卡交会对接华看似简单爱空间和我带我就挖"
					},
					{
						"class_number":"4",
						"number":"2",
						"date":"1",
						"reason":"神盾局群殴IU欧文我空间还澳际丶好好说"
					},
				]
			}
		},
		onLoad() {
			var that=this
			// uni.request({
			// 	header: {
			// 	   'content-type':'application/x-www-form-urlencoded'},
			// 	url:getApp().globalData.urlRoot+"manager/Loadmanager",
			// 	method:'POST',
			// 	data:{
					
			// 	},
			// 	success: (res) => {
			// 		that.table_data=res.data.form
			// 	},
			// 	fail() {
			// 		uni.showToast({
			// 			title: "获取失败！",
			// 			icon: 'none'
			// 		})
			// 	}
			// })
		},
		methods: {
			
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
