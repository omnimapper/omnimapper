#include <boost/python.hpp>
#include <iostream>

void register_module() 
{
	std::cout << "Hello Blender from C++!\n";
}

void unregister_module()
{
	std::cout << "Goodbye Blender from C++!\n";
}

BOOST_PYTHON_MODULE(omnimappercpp)
{
	using namespace boost::python;
	def("register", register_module);
	def("unregister", unregister_module);
}
