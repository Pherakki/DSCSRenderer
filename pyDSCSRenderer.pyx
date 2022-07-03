from libcpp.string cimport string

cdef extern from "<array>" namespace "std" nogil:
    cdef cppclass farray3 "std::array<float, 3>":
        farray3() except+
        float& operator[](size_t)
    
cdef extern from "src/DSCS/RenderObjects/Camera.hpp":
    cdef cppclass Camera:
        Camera() except +

        void setPosition(farray3& pos)
        void setTarget(farray3& pos)
        void incPosition(farray3& inc)
        void incTarget(farray3& inc)
        void incPosAndTarget(farray3& inc)
        
        

        void translate(float x, float y)
        void mulRadius(float fac)
        void incAltAzi(float aziInc, float altInc)

cdef extern from "src/DSCS/Renderer.hpp" namespace "Rendering::DSCS":    
    cdef cppclass Renderer:
        Renderer() except +
        
        float aspect_ratio
        float clock_time
        float delta_time

        Camera camera
        
        void initRenderer()
        void refreshRenderSettings()
        void recalculateGlobalUniforms()
        int loadModel(const string& path)
        void loadAnim(int model_id, const string& anim_path)
        void render()
        void advTime(float adv)

cdef class DSCSRenderer:
    cdef Renderer* thisptr
    def __cinit__(self):
        self.thisptr = new Renderer()
        self.thisptr.aspect_ratio = 4/3
        self.thisptr.clock_time = 0
        self.thisptr.delta_time = 0
        
    def __dealloc__(self):
        del self.thisptr
    def initRenderer(self):
        self.thisptr.initRenderer()
    def refreshRenderSettings(self):
        self.thisptr.refreshRenderSettings()
    def recalculateGlobalUniforms(self):
        self.thisptr.recalculateGlobalUniforms()
    def render(self):
        self.thisptr.render()
    def advanceClock(self, adv):
        self.thisptr.advTime(adv)
    def loadModel(self, filepath):
        return self.thisptr.loadModel(filepath.encode("utf8"))
    def loadAnim(self, model_id, filepath):
        self.thisptr.loadAnim(model_id, filepath.encode("utf8"))
    def setAspectRatio(self, width, height):
        self.thisptr.aspect_ratio = width/height
    def setCameraPosition(self, x, y, z):
        cdef farray3 arr = farray3()
        arr[0] = x
        arr[1] = y
        arr[2] = z
        self.thisptr.camera.setPosition(arr)
    def setCameraTarget(self, x, y, z):
        cdef farray3 arr = farray3()
        arr[0] = x
        arr[1] = y
        arr[2] = z
        self.thisptr.camera.setTarget(arr)
    def translateCamera(self, x, y):
        self.thisptr.camera.translate(x, y)
    def rotateOrbitCamera(self, alt, azi):
        self.thisptr.camera.incAltAzi(alt, azi)
    def zoomCamera(self, distance):
        self.thisptr.camera.mulRadius(distance)
