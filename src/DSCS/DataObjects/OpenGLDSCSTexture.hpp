#pragma once
#include <filesystem>
#include <string>
#include "../../FileFormats/Textures/DDS.hpp"

namespace Rendering::DataObjects
{
	class OpenGLDSCSTexture
	{
	public:
		OpenGLDSCSTexture(const std::filesystem::path& filepath, TextureType tex_type);
		~OpenGLDSCSTexture();

		std::string img_name;
		TextureType tex_type;

		unsigned int getBufferID();
	private:
		unsigned int buffer_id;
	};

}
