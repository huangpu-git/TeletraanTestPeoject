<template>
  <div class="uploadImg" >
    <div style="text-align:center">
      <el-upload
        ref="uploadImg"
        width="200px"
        drag
        action="#"
        :limit="limitNum"
        :auto-upload="false"
        accept=".jpg,.png"
        :before-upload="beforeUploadFile"
        :on-change="fileChange"
        :on-exceed="exceedFile"
        :on-success="handleSuccess"
        :on-error="handleError"
        :file-list="fileList">
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        <div slot="tip" class="el-upload__tip">
          只能上传.jpg/.png的图片，且不超过10M
        </div>
      </el-upload>
      <el-button size="small" type="primary" style="margin-top:20px" @click="uploadFile">
        解析图片
      </el-button>
      <el-button size="small">
        取消
      </el-button>
    </div>
    <span style="margin-top:20px">识别结果为： {{ img_content }}</span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      limitNum: 10,
      formLabelWidth: "80px",
      form: {
        file: ""
      },
      fileList: [],
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      img_content: ""
    }
  },
  methods: {
    // 文件超出个数限制时的钩子
    exceedFile(files, fileList) {
      this.$notify.warning({
        title: "警告",
        message: `只能选择 ${this.limitNum} 个文件，当前共选择了 ${files.length + fileList.length} 个`
      });
    },
    // 文件状态改变时的钩子
    fileChange(file, fileList) {
      console.log('change')
      console.log(file)
      this.form.file = file.raw
      console.log(fileList)
    },
    // 上传文件之前的钩子, 参数为上传的文件,若返回 false 或者返回 Promise 且被 reject，则停止上传
    beforeUploadFile(file) {
      console.log('before upload')
      console.log(file)
      let extension = file.name.substring(file.name.lastIndexOf('.')+1)
      let size = file.size / 1024 / 1024
      if(extension !== 'jpg'|| extension !== 'png') {
        this.$notify.warning({
          title: '警告',
          message: `只能上传图片（即后缀是.jpg或者.png）的文件`
        });
      }
      if(size > 10) {
        this.$notify.warning({
          title: '警告',
          message: `文件大小不得超过10M`
        });
      }
    },
    // 文件上传成功时的钩子
    handleSuccess(res, file, fileList) {
      this.$notify.success({
        title: '成功',
        message: `文件上传成功`
      });
    },
    // 文件上传失败时的钩子
    handleError(err, file, fileList) {
      this.$notify.error({
        title: '错误',
        message: `文件上传失败`
      });
    },
    uploadFile() {
      let param = new FormData();
      console.log(this.form.file)
      param.append("uploadFile", this.form.file)
      console.log(param)
      this.$axios.post("http://192.168.101.107:8999/upload_img", param, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(responce => {
        this.img_content = responce.data
      });
      this.$message({
        message: "上传成功！",
        duration: 1000
      });
    }
  }
}
</script>

<style lang="scss" scoped>
</style>