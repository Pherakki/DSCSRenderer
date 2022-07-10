#include "OpenGLDSCSTexture.hpp"

#include "../../../libs/glad/include/glad/glad.h"


namespace Rendering::DataObjects
{
	OpenGLDSCSTexture::OpenGLDSCSTexture(const std::filesystem::path& filepath, TextureType tex_type)
	{
		this->buffer_id = loadDDS(filepath.string().c_str(), tex_type);
		this->img_name = filepath.string();
		this->tex_type = tex_type;
	}

	OpenGLDSCSTexture::~OpenGLDSCSTexture()
	{
		glDeleteTextures(1, &this->buffer_id);
	}

	GLuint OpenGLDSCSTexture::getBufferID()
	{
		return this->buffer_id;
	}
}