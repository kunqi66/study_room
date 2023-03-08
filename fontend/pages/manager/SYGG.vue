<template>
	<view>
		<uni-section title="编辑公告:" type="line"></uni-section>
<uni-table ref="table" :loading="loading" border stripe emptyText="请输入新增规定" @selection-change="selectionChange">
	                 <uni-tr>
	                 	<uni-th width="50" align="center">标题</uni-th>
	                 	<uni-th width="200" align="center">内容</uni-th>
	                 	<uni-th align="center">日期</uni-th>
	                 </uni-tr>
					<uni-tr v-for="(item, index) in combDate" :key="index">
						<uni-td align="center">{{ combDate[index].title }}</uni-td>
						<uni-td align="center">{{ combDate[index].text }}</uni-td>
						<uni-td align="center">{{ combDate[index].date }}</uni-td>
					</uni-tr>
					
					
					</uni-table>
					
					
					<uni-popup ref="editData">
						<uni-forms ref="form" :modelValue="formData" >
					<uni-forms-item label="标题" name="title">
							<uni-easyinput  type="text" v-model="formData.title" >
							</uni-easyinput>
						</uni-forms-item>
						<uni-forms-item label="内容" name="text">
							<uni-easyinput type="text" v-model="formData.text" >
							</uni-easyinput>
						</uni-forms-item>
						<uni-forms-item label="日期" name="date">
							<uni-easyinput  type="text" v-model="formData.number" >
							</uni-easyinput>
						</uni-forms-item>
					</uni-forms>	
						</uni-popup>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				formData:{},
				combDate:[{
					"title":"书上",
					"text":"风格",
					"date":"789"
				},{
					"title":"书上",
					"text":"风格",
					"date":"789"
				}],
				editData:false,
			}
		
		
	},
	onLoad() {
		var that=this
		uni.request({
			header: { 'content-type':'application/x-www-form-urlencoded'},
			url:getApp().globalData.urlRoot+"",
			method:'POST',
			data:{
				
			},
			success: (res) => {
						if(res.data.suc){
							console.log("添加成功")
							that.combDate=res.data.form
							console.log(that.combDate[0].mana)
							console.log(res.data.form)
						}else{
							console.log("添加失败")
							console.log(res.data.message)
						}
					},
					fail() {
						uni.showToast({
							title: "错误！",
							icon: 'none'
						})
					}
				})
			},
			   methods: {
			   	SubmitEdit(){
			   		var that=this;
			   		uni.request({
			   			url:getApp().globalData.urlRoot+"manager/SYGG",
						header: {'Authorization':getApp().globalData.token,
						   'content-type':''},
						   data:{
						   	"title":that.formData.title,
							"text":that.formData.text,
							"date":that.formData.date,
						   },
						   method:"POST",
						   		success(res) {
						   			if(res.data.suc){
						   				uni.showToast({
						   					title: String(res.data.message),
						   					icon: 'checkmarkempty'
						   				})
						   				uni.navigateTo({
						   					url: "/pages/manager/SYGG",
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

</style>