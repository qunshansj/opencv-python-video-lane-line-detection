
lines = cv2.HoughLinesP(edge_img,  1, np.pi / 180, 15, minLineLength=40, maxLineGap=20)
