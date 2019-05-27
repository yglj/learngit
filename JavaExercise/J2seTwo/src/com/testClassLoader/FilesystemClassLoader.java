package com.testClassLoader;

import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

public class FilesystemClassLoader extends ClassLoader{
	private String rootdir;
	public FilesystemClassLoader(String path) {
		// TODO Auto-generated constructor stub
		this.rootdir = path;
	}
	@Override
	protected Class<?> findClass(String name) throws ClassNotFoundException {
		// TODO Auto-generated method stub
		Class<?> c =findLoadedClass(name);
		if(c != null){
			return c;
		}
		else{
			ClassLoader parent = this.getParent();

				c = parent.loadClass(name);

			if( c != null){
				return c;
			}
			else{
				byte[] classDate = null;

					try {
						classDate = getClassDate(name);
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}

				if(classDate == null){
					throw new ClassNotFoundException();
				}
				else{
					c = defineClass(name, classDate, 0, classDate.length);
				}
			}
		}
		return c;
	}
	private byte[] getClassDate(String classname) throws IOException{
		String path = rootdir + "/" + classname.replace(".","/")+".class";
		InputStream is = null ;
		ByteArrayOutputStream bos = null;
		try {
			is = new FileInputStream(path);
			bos = new ByteArrayOutputStream();
			byte[] buffer = new byte[1024];
			int temp = 0;
			while((temp = is.read(buffer)) != -1){
				bos.write(temp);
			}
			return bos.toByteArray();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return null;
		}finally{
			if(is != null){
				is.close();
			}
			if(bos != null){
				bos.close();
			}
		}	
	}
}
