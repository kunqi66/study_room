<template>
	<view>
		<uni-section title="个人信息" type="line">
		<uni-list>
			<uni-list-item title="姓名" :rightText="user2.name" />
			<uni-list-item title="学号" :rightText="user2.student_number" />
		</uni-list>
		<uni-forms ref="baseForm" :modelValue="baseFormData">
			<uni-forms-item label="电话" required>
				<uni-easyinput v-model="baseFormData.number" placeholder="请输入修改后的电话" />
			</uni-forms-item>
		</uni-forms>
		</uni-section>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				user2:{
					name:'',
					student_number:'',
				},
				baseFormData:{
					number:-1
				}
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
