#!/usr/bin/env python3
"""Generates ArUco marker with defined ID and size."""

import cv2

MARKER_ID = 33          # ID метки (0–50 для Dict 4x4)
MARKER_SIZE_PX = 600   # размер PNG в пикселях (квадрат)
DICT = cv2.aruco.DICT_4X4_50  # словарь

aruco_dict = cv2.aruco.getPredefinedDictionary(DICT)
marker = cv2.aruco.generateImageMarker(aruco_dict, MARKER_ID, MARKER_SIZE_PX)

# Добавляем белый бордер 10% для лучшего детектирования
border = int(MARKER_SIZE_PX * 0.1)
marker_bordered = cv2.copyMakeBorder(
    marker, border, border, border, border,
    cv2.BORDER_CONSTANT, value=255
)

cv2.imwrite(f"../models/aruco_marker/materials/textures/aruco_4x4_{MARKER_ID}.png", marker_bordered)
print(f"Saved: aruco_4x4_{MARKER_ID}.png ({marker_bordered.shape[1]}x{marker_bordered.shape[0]})")
