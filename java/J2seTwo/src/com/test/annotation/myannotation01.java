package com.test.annotation;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

import javax.lang.model.element.Element;

@SuppressWarnings("unused")
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
public @interface myannotation01 {
	String value();
}
