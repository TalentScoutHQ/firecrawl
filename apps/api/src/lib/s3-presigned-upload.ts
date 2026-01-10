import axios from "axios";
import type { Logger } from "winston";
import type { ScrapeJobData } from "../types";

type DocumentUpload = NonNullable<ScrapeJobData["documentUpload"]>;

export async function uploadJsonToPresignedUrl(
  upload: DocumentUpload,
  payload: unknown,
  logger: Logger,
  context?: { jobId?: string; url?: string },
) {
  const headers: Record<string, string> = { ...(upload.headers ?? {}) };
  const hasContentType = "Content-Type" in headers || "content-type" in headers;
  if (!hasContentType) {
    headers["Content-Type"] = upload.contentType ?? "application/json";
  }

  const body = JSON.stringify(payload);

  try {
    const response = await axios.put(upload.presignedUrl, body, {
      headers,
      maxBodyLength: Infinity,
      maxContentLength: Infinity,
      validateStatus: status => status >= 200 && status < 300,
    });

    logger.info("Uploaded crawled document to presigned URL", {
      jobId: context?.jobId,
      url: context?.url,
      status: response.status,
    });
  } catch (error) {
    logger.warn("Failed to upload crawled document to presigned URL", {
      jobId: context?.jobId,
      url: context?.url,
      error,
    });
  }
}
