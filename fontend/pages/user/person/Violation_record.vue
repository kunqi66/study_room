<template>
	<view>
		<view class="title">
			个人违规记录
		</view>
		<view class="uni-container">
			<uni-table ref="com_table" :loading="loading" border stripe emptyText="暂无更多数据" @selection-change="selectionChange">
							<uni-tr>
								<uni-th width="70" align="center">教室号</uni-th>
								<uni-th width="70" align="center">座位号</uni-th>
								<uni-th width="70" align="center">日期</uni-th>
								<uni-th width="200" align="center">违规原因</uni-th>
							</uni-tr>
							<uni-tr v-for="(item, index) in violationlist" :key="index">
								<uni-td align="center" class="td">{{ violationlist[index].classnumber }}</uni-td>
								<uni-td align="center" class="td">{{ violationlist[index].sitnumber }}</uni-td>
								<uni-td align="center" class="td">{{ violationlist[index].date }}</uni-td>
								<uni-td align="center" class="td">{{ violationlist[index].reason }}</uni-td>
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
				violationlist:[{
					"classnumber":"2213",
					"sitnumber":"23123",
					"date":"2131",
					"reason":"231424"
				},
				{
					"classnumber":"2213",
					"sitnumber":"23123",
					"date":"2131",
					"reason":"231424"
				},
				{
					"classnumber":"2213",
					"sitnumber":"23123",
					"date":"2131",
					"reason":"231424"
				},]
			}
		},
		methods: {
			
		}
	}
</script>

<style>
	.title{
		font-size: 16px;
		border-left: 5px solid #ff0000;
		padding-left: 10px;
		margin-top: 10px;
		margin-bottom: 10px;
	}
</style>
